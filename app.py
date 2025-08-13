import os
import torch
import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM, TextIteratorStreamer
import re
import threading

# Import configuration and templates
from config import *
from templates import TEMPLATES
from utils import load_css

# Pre-load model in global scope
print("Loading model...")
tokenizer = AutoTokenizer.from_pretrained(
    REPO_ID,
    cache_dir=CACHE_DIR,
)
model = AutoModelForCausalLM.from_pretrained(
    REPO_ID,
    cache_dir=CACHE_DIR,
    torch_dtype="auto",
    device_map="auto",
)
print("Model loaded successfully!")


def format_output(text: str) -> str:
    """Format model output, extract thought chain and final answer"""
    if not text:
        return ""

    # Use regular expressions to extract analysis and final parts
    analysis_complete_pattern = r"<\|channel\|>analysis<\|message\|>(.*?)<\|end\|>"
    analysis_partial_pattern = r"<\|channel\|>analysis<\|message\|>(.*)"
    final_pattern = (
        r"<\|start\|>assistant<\|channel\|>final<\|message\|>(.*?)(?:<\|return\|>|$)"
    )

    # For streaming support: partial final pattern (without end marker)
    partial_final_pattern = r"<\|start\|>assistant<\|channel\|>final<\|message\|>(.*)"

    analysis_complete_match = re.search(analysis_complete_pattern, text, re.DOTALL)
    analysis_partial_match = re.search(analysis_partial_pattern, text, re.DOTALL)
    final_match = re.search(final_pattern, text, re.DOTALL)

    formatted_output = ""

    # Handle analysis part
    if analysis_complete_match:
        # Analysis is complete, show it in collapsible format
        analysis_text = analysis_complete_match.group(1).strip()
        if analysis_text:
            # Clean up analysis text and make it more readable
            analysis_text = re.sub(r"\s+", " ", analysis_text)  # Normalize whitespace
            formatted_output += f"<details>\n<summary>💭 <strong>Thinking Process</strong></summary>\n\n> {analysis_text}\n\n</details>\n\n"

    elif analysis_partial_match:
        # Analysis is in progress, show it with title but not collapsed
        analysis_text = analysis_partial_match.group(1).strip()
        if analysis_text:
            # Clean up analysis text and make it more readable
            analysis_text = re.sub(r"\s+", " ", analysis_text)  # Normalize whitespace
            formatted_output += f"💭 **Thinking Process:**\n\n> {analysis_text}\n\n"

    # Extract and format final part
    if final_match:
        final_text = final_match.group(1).strip()
        if final_text:
            # Preserve original formatting for the final answer
            formatted_output += final_text
    else:
        # Fallback 1: try simpler final pattern without <|start|>assistant
        simple_final_pattern = r"<\|channel\|>final<\|message\|>(.*?)(?:<\|return\|>|$)"
        simple_final_match = re.search(simple_final_pattern, text, re.DOTALL)
        if simple_final_match:
            final_text = simple_final_match.group(1).strip()
            if final_text:
                formatted_output += final_text
        else:
            # Fallback 2: for streaming, check if we have partial final content
            partial_match = re.search(partial_final_pattern, text, re.DOTALL)
            if partial_match:
                final_text = partial_match.group(1).strip()
                if final_text:
                    formatted_output += final_text

    # If no special format is matched, return original text (clean special characters)
    if not formatted_output:
        # Clean all special markers but preserve the content structure
        cleaned_text = re.sub(r"<\|[^|]*\|>", "", text)
        # Remove extra whitespace but preserve line breaks
        cleaned_text = re.sub(r"\n\s*\n\s*\n", "\n\n", cleaned_text)
        formatted_output = cleaned_text.strip()

    return formatted_output


def infer_stream(prompt: str):
    """Generator function for streaming inference"""
    if not prompt or not prompt.strip():
        yield ""
        return

    # Use chat template format
    messages = [
        {"role": "user", "content": prompt},
    ]

    inputs = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=True,
        return_dict=True,
        return_tensors="pt",
    ).to(model.device)

    # Create streamer
    streamer = TextIteratorStreamer(
        tokenizer, timeout=30, skip_prompt=True, skip_special_tokens=False
    )

    # Generation parameters
    generation_kwargs = dict(
        **inputs,
        max_new_tokens=tokenizer.model_max_length,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id,
        streamer=streamer,
    )

    # Start generation in a separate thread
    thread = threading.Thread(target=model.generate, kwargs=generation_kwargs)
    thread.start()

    # Stream the output
    generated_text = ""
    for new_text in streamer:
        generated_text += new_text
        # Format and yield the current output
        formatted_text = format_output(generated_text)
        yield formatted_text

    # Ensure thread completion
    thread.join()


def clear_inputs():
    """Clear input textbox"""
    return ""


with gr.Blocks(css=load_css(), title=APP_TITLE, theme=gr.themes.Soft()) as demo:
    # Title
    gr.HTML(TEMPLATES["title"])

    with gr.Row(equal_height=True):
        # Left side: Input area
        with gr.Column(scale=1, min_width=400):
            # Input area with container for consistent height
            with gr.Group():
                gr.HTML(TEMPLATES["input_section_title"])
                prompt_input = gr.Textbox(
                    label="",
                    placeholder=DEFAULT_PROMPT_PLACEHOLDER,
                    lines=12,  # Increased from 10 to better match right side height
                    max_lines=15,
                    container=True,
                    show_label=False,
                )

            # Action buttons
            with gr.Row():
                generate_btn = gr.Button(
                    "🎯 Generate Reply", variant="primary", size="lg"
                )
                clear_btn = gr.Button("🗑️ Clear", variant="secondary", size="lg")

        # Right side: Output area
        with gr.Column(scale=1, min_width=400):
            # Output area with container to match left side structure
            with gr.Group():
                gr.HTML(TEMPLATES["output_title"])
                output = gr.Markdown(
                    value=DEFAULT_OUTPUT_MESSAGE,
                    elem_classes=["output-container"],
                    container=True,
                    height=450,  # Increased height to match left side total height
                )

    # Example prompts section
    gr.HTML(TEMPLATES["examples_title"])
    gr.HTML(TEMPLATES["examples_description"])

    examples = gr.Examples(
        examples=EXAMPLE_PROMPTS,
        inputs=prompt_input,
        examples_per_page=4,
    )

    # Event binding - use streaming output
    generate_btn.click(
        fn=infer_stream, inputs=[prompt_input], outputs=output, show_progress=True
    )
    clear_btn.click(fn=clear_inputs, inputs=[], outputs=[prompt_input])

    # Add footer
    gr.HTML(TEMPLATES["footer"])

if __name__ == "__main__":
    demo.launch()
