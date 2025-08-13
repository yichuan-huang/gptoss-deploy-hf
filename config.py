# Configuration file
import os

# Model configuration
REPO_ID = "openai/gpt-oss-20b"
CACHE_DIR = "../huggingface_cache"  # Change to your desired cache directory

# UI configuration
APP_TITLE = "GPT-OSS 20B Demo"
DEFAULT_PROMPT_PLACEHOLDER = """Please enter your question or prompt...

Examples:
• Who are you?
• Explain the basic concepts of machine learning
• Write a poem about spring"""

DEFAULT_OUTPUT_MESSAGE = """AI response will be displayed here...

💡 **Tip:** The model's thinking process will be shown in quote format, with the final answer below."""

# Example prompts
EXAMPLE_PROMPTS = [
    ["Who are you?"],
    ["Explain what deep learning is and its applications in real life"],
    ["Write a short story about future technology development"],
    ["Help me create a plan for learning Python programming"],
    ["Analyze the development prospects of renewable energy"],
]

# Server configuration
SERVER_NAME = "0.0.0.0"
SERVER_PORT = 7860
SHARE = False
SHOW_ERROR = True

# CSS file path
CSS_FILE_PATH = "./static/styles.css"
