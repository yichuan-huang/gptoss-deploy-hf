# GPT-OSS 20B Model Deployment with Huggingface and Gradio

This project provides a simple and interactive web interface for the GPT-OSS 20B language model using Gradio. It offers a clean, user-friendly chat interface that allows users to interact with the model and view its responses, including its internal "thought process."

## Features

- **Interactive Chat Interface**: A clean and intuitive web UI for chatting with the GPT-OSS 20B model.
- **Optimized Generation**: The model uses optimal generation parameters with no token limit restrictions, allowing for comprehensive responses.
- **Thought Process Visualization**: The model's output is formatted to separate the final answer from its internal "thinking" or analysis steps, providing insight into how it arrived at the answer.
- **Example Prompts**: Includes a set of example prompts in English to help users get started quickly.
- **Easy to Deploy**: Built with Gradio for simple deployment as a web application.
- **Multi-GPU Support**: Automatically utilizes available GPUs for optimal performance.

## How to Use

1.  **Install Dependencies**:
    Install the required Python packages using pip:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Application**:
    
    **Standard deployment (without mxfp4 triton backend):**
    ```bash
    python app.py
    ```
    
    **For multi-GPU deployment, you can specify which GPUs to use, for example:**
    ```bash
    CUDA_VISIBLE_DEVICES=0,1,2,3 python app.py
    ```
    
    The application will be available at the local URL provided in the terminal (e.g., `http://127.0.0.1:7860`).

3.  **Interact with the Model**:
    - Open the URL in your web browser.
    - Type your prompt into the input text box.
    - Click the "🎯 Generate Reply" button to get a response from the model.
    - Use the "🗑️ Clear" button to reset the input field.
    - Try the example prompts provided below the interface for quick start.

## Model Configuration

The application uses optimized settings for the best user experience:

- **No Token Limits**: The model can generate responses up to its maximum context length without artificial restrictions.
- **Optimal Parameters**: Uses carefully tuned temperature and top-p values for balanced creativity and coherence.
- **Automatic GPU Detection**: Automatically distributes the model across available GPUs for optimal performance.

## Requirements

This project relies on the following main libraries:

- `transformers`: For loading and using the GPT-OSS 20B pre-trained language model.
- `torch`: The underlying deep learning framework.
- `accelerate`: To optimize model loading and execution on available hardware.
- `gradio`: For creating the interactive web interface.
- `sentencepiece`: A tokenizer used by the model.
- `protobuf`: A dependency for model serialization.

All required packages are listed in the `requirements.txt` file.

## Configuration

The application can be configured through the `config.py` file:

- **Model Settings**: Specify the model repository ID and cache directory.
- **UI Settings**: Customize the application title, placeholders, and example prompts.
- **Server Settings**: Configure the server host, port, and sharing options.

## File Structure

```
├── app.py              # Main application file
├── config.py           # Configuration settings
├── templates.py        # HTML templates for the UI
├── utils.py           # Utility functions
├── requirements.txt    # Python dependencies
├── static/
│   └── styles.css     # Custom CSS styles
└── README.md          # This file
```

## Features in Detail

### Thought Process Visualization
The model outputs are formatted to show:
- **Thinking Process**: The model's internal analysis and reasoning steps
- **Final Answer**: The conclusive response to the user's query

### Multi-language Support
The interface supports English:
- UI elements are in English for better accessibility
- Example prompts are in English
- The model can understand and respond in multiple languages

### Optimized Performance
- Automatic device mapping for multi-GPU setups
- Efficient memory usage with proper model loading
- Streamlined generation without unnecessary parameter exposure

## Troubleshooting

If you encounter any issues:

1. **Memory Issues**: Ensure you have sufficient GPU memory (recommended: 40GB+ VRAM)
2. **Model Loading**: Check that the cache directory has enough space
3. **Dependencies**: Make sure all packages are installed correctly with `pip install -r requirements.txt`
4. **GPU Detection**: Verify CUDA availability with `python -c "import torch; print(torch.cuda.is_available())"`