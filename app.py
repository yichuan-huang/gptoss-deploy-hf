import os
import torch
import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM
import re

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
    device_map="auto",
)
print("Model loaded successfully!")


def format_output(text: str) -> str:
    """Format model output, extract thought chain and final answer"""
    if not text:
        return ""

    # Use regular expressions to extract analysis and final parts
    analysis_pattern = r"<\|channel\|>analysis<\|message\|>(.*?)<\|end\|>"
    final_pattern = r"<\|channel\|>final<\|message\|>(.*?)<\|return\|>"

    analysis_match = re.search(analysis_pattern, text, re.DOTALL)
    final_match = re.search(final_pattern, text, re.DOTALL)

    formatted_output = ""

    # Extract and format analysis part
    if analysis_match:
        analysis_text = analysis_match.group(1).strip()
        if analysis_text:
            formatted_output += f"> **Thinking Process:** {analysis_text}\n\n"

    # Extract and format final part
    if final_match:
        final_text = final_match.group(1).strip()
        if final_text:
            formatted_output += final_text

    # If no special format is matched, return original text (clean special characters)
    if not formatted_output:
        # Clean all special markers
        cleaned_text = re.sub(r"<\|[^|]*\|>", "", text)
        formatted_output = cleaned_text.strip()

    return formatted_output


def infer(prompt: str) -> str:
    if not prompt or not prompt.strip():
        return ""

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

    outputs = model.generate(
        **inputs,
        max_new_tokens=tokenizer.model_max_length,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id,
    )

    text = tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1] :])

    # Format output
    formatted_text = format_output(text)
    return formatted_text


def clear_inputs():
    return ""


# Create interface
with gr.Blocks(css=load_css(), title=APP_TITLE, theme=gr.themes.Soft()) as demo:
    # Title
    gr.HTML(TEMPLATES["title"])

    with gr.Row():
        # Left side: Input area
        with gr.Column(scale=1):
            # Input area
            gr.HTML(TEMPLATES["input_section_title"])
            prompt_input = gr.Textbox(
                label="",
                placeholder=DEFAULT_PROMPT_PLACEHOLDER,
                lines=8,
            )

            # Buttons
            with gr.Row():
                generate_btn = gr.Button("🎯 Generate Reply", variant="primary")
                clear_btn = gr.Button("🗑️ Clear", variant="secondary")

        # Right side: Output
        with gr.Column(scale=1):
            gr.HTML(TEMPLATES["output_title"])
            output = gr.Markdown(
                value=DEFAULT_OUTPUT_MESSAGE,
                elem_classes=["output-container"],
            )

    # Example prompts
    gr.HTML(TEMPLATES["examples_title"])
    gr.HTML(TEMPLATES["examples_description"])

    examples = gr.Examples(
        examples=EXAMPLE_PROMPTS,
        inputs=prompt_input,
    )

    # Event binding
    generate_btn.click(fn=infer, inputs=[prompt_input], outputs=output)

    clear_btn.click(fn=clear_inputs, inputs=[], outputs=[prompt_input])

    # Add footer
    gr.HTML(TEMPLATES["footer"])

if __name__ == "__main__":
    demo.launch(
        server_name=SERVER_NAME,
        server_port=SERVER_PORT,
        share=SHARE,
        show_error=SHOW_ERROR,
    )
