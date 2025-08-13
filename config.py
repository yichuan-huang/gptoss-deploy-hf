# Configuration file
import os

# Model configuration
REPO_ID = "openai/gpt-oss-20b"
CACHE_DIR = "../huggingface_cache"  # Change to your desired cache directory

# UI configuration
APP_TITLE = "GPT-OSS 20B Demo"
DEFAULT_PROMPT_PLACEHOLDER = """🎯 Enter your question or prompt here...

💡 Try these ideas:
• Ask me about artificial intelligence and machine learning
• Request creative writing like stories or poems  
• Get help with programming and technical questions
• Explore complex topics with detailed explanations
• Chat about current events or philosophical topics

✨ Watch my thinking process unfold in real-time!"""

DEFAULT_OUTPUT_MESSAGE = """🤖 **AI Response Area**

Your intelligent response will appear here with full thought chain visualization.

💭 **What you'll see:**
- My thinking process in highlighted quote blocks
- Step-by-step reasoning and analysis  
- Final comprehensive answer

🚀 **Ready to explore AI intelligence?** Enter a prompt above to get started!"""

# Enhanced example prompts
EXAMPLE_PROMPTS = [
    ["Who are you and what makes you special?"],
    ["Explain quantum computing in simple terms with real-world applications"],
    ["Write a creative short story about AI and humans working together in 2030"],
    ["Help me create a comprehensive learning plan for mastering Python programming"],
    ["Analyze the future of renewable energy and its impact on climate change"],
    ["What are the ethical implications of advanced AI systems?"],
    ["Describe how blockchain technology could revolutionize different industries"],
    ["Create a poem about the beauty of mathematics and science"],
]

# CSS file path
CSS_FILE_PATH = "./static/styles.css"
