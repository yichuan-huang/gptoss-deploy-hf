# HTML template definitions with elegant colors
TEMPLATES = {
    "title": """
        <div style="text-align: center; margin-bottom: 40px; position: relative;">
            <div style="
                position: absolute;
                top: -20px;
                left: 50%;
                transform: translateX(-50%);
                width: 100px;
                height: 3px;
                background: linear-gradient(45deg, #10b981, #3b82f6, #f59e0b);
                border-radius: 2px;
                opacity: 0.7;
            "></div>
            <h1 style="
                background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                font-size: 3.5rem;
                font-weight: 700;
                margin-bottom: 16px;
                letter-spacing: -0.02em;
                line-height: 1.1;
                font-family: 'Inter', sans-serif;
            ">🚀 GPT-OSS 20B</h1>
            <div style="
                background: rgba(255, 255, 255, 0.9);
                border-radius: 50px;
                padding: 12px 32px;
                display: inline-block;
                border: 1px solid rgba(102, 126, 234, 0.2);
                backdrop-filter: blur(10px);
                margin-bottom: 20px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
            ">
                <p style="
                    color: #64748b; 
                    font-size: 1.2rem; 
                    margin: 0;
                    font-weight: 500;
                    letter-spacing: 0.01em;
                ">Experience the powerful open-source language model</p>
            </div>
            <div style="
                display: flex;
                justify-content: center;
                gap: 16px;
                flex-wrap: wrap;
                margin-top: 20px;
            ">
                <div style="
                    background: rgba(16, 185, 129, 0.1);
                    padding: 8px 16px;
                    border-radius: 20px;
                    color: #059669;
                    font-weight: 600;
                    font-size: 0.9rem;
                    border: 1px solid rgba(16, 185, 129, 0.2);
                ">🧠 Thought Chain</div>
                <div style="
                    background: rgba(59, 130, 246, 0.1);
                    padding: 8px 16px;
                    border-radius: 20px;
                    color: #2563eb;
                    font-weight: 600;
                    font-size: 0.9rem;
                    border: 1px solid rgba(59, 130, 246, 0.2);
                ">⚡ Real-time</div>
                <div style="
                    background: rgba(245, 158, 11, 0.1);
                    padding: 8px 16px;
                    border-radius: 20px;
                    color: #d97706;
                    font-weight: 600;
                    font-size: 0.9rem;
                    border: 1px solid rgba(245, 158, 11, 0.2);
                ">🔓 Open Source</div>
            </div>
        </div>
    """,
    "input_section_title": """
        <div style="
            display: flex;
            align-items: center;
            margin-bottom: 20px;
            padding-bottom: 12px;
            border-bottom: 2px solid rgba(16, 185, 129, 0.1);
        ">
            <div style="
                width: 40px;
                height: 40px;
                background: linear-gradient(135deg, #10b981, #059669);
                border-radius: 12px;
                display: flex;
                align-items: center;
                justify-content: center;
                margin-right: 12px;
                box-shadow: 0 4px 8px rgba(16, 185, 129, 0.2);
            ">
                <span style="font-size: 20px; color: white;">💬</span>
            </div>
            <h3 style="
                margin: 0; 
                color: #374151;
                font-size: 1.4rem;
                font-weight: 700;
                letter-spacing: -0.01em;
            ">Input Prompt</h3>
        </div>
    """,
    "output_title": """
        <div style="
            display: flex;
            align-items: center;
            margin-bottom: 20px;
            padding-bottom: 12px;
            border-bottom: 2px solid rgba(59, 130, 246, 0.1);
        ">
            <div style="
                width: 40px;
                height: 40px;
                background: linear-gradient(135deg, #3b82f6, #2563eb);
                border-radius: 12px;
                display: flex;
                align-items: center;
                justify-content: center;
                margin-right: 12px;
                box-shadow: 0 4px 8px rgba(59, 130, 246, 0.2);
            ">
                <span style="font-size: 20px; color: white;">🤖</span>
            </div>
            <h3 style="
                margin: 0; 
                color: #374151;
                font-size: 1.4rem;
                font-weight: 700;
                letter-spacing: -0.01em;
            ">AI Response</h3>
        </div>
    """,
    "examples_title": """
        <div style="
            display: flex;
            align-items: center;
            margin: 40px 0 20px 0;
            padding-bottom: 16px;
            border-bottom: 2px solid rgba(245, 158, 11, 0.1);
        ">
            <div style="
                width: 48px;
                height: 48px;
                background: linear-gradient(135deg, #f59e0b, #d97706);
                border-radius: 16px;
                display: flex;
                align-items: center;
                justify-content: center;
                margin-right: 16px;
                box-shadow: 0 6px 12px rgba(245, 158, 11, 0.2);
            ">
                <span style="font-size: 24px; color: white;">💡</span>
            </div>
            <h3 style="
                margin: 0; 
                color: #374151;
                font-size: 1.6rem;
                font-weight: 700;
                letter-spacing: -0.01em;
            ">Example Prompts</h3>
        </div>
    """,
    "examples_description": """
        <div style="
            background: rgba(255, 255, 255, 0.8);
            border-radius: 20px;
            padding: 24px;
            border: 1px solid rgba(102, 126, 234, 0.1);
            margin-bottom: 24px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
            backdrop-filter: blur(10px);
        ">
            <div style="
                display: flex;
                align-items: center;
                margin-bottom: 12px;
            ">
                <div style="
                    width: 32px;
                    height: 32px;
                    background: linear-gradient(135deg, #667eea, #764ba2);
                    border-radius: 8px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin-right: 12px;
                ">
                    <span style="font-size: 16px; color: white;">✨</span>
                </div>
                <h4 style="
                    margin: 0;
                    color: #374151;
                    font-weight: 600;
                    font-size: 1.1rem;
                ">Quick Start</h4>
            </div>
            <p style="
                margin: 0; 
                color: #64748b;
                font-size: 1rem;
                line-height: 1.6;
                font-weight: 500;
            ">Click any example below to get started instantly. Each prompt supports thought chain visualization to show the AI's reasoning process.</p>
        </div>
    """,
    "footer": """
        <div style="
            text-align: center;
            margin-top: 50px;
            padding: 30px 20px 20px;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 24px;
            border: 1px solid rgba(102, 126, 234, 0.1);
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.05);
        ">
            <div style="
                display: flex;
                justify-content: center;
                gap: 30px;
                flex-wrap: wrap;
                margin-bottom: 20px;
            ">
                <div style="
                    display: flex;
                    align-items: center;
                    gap: 8px;
                    color: #10b981;
                    font-weight: 600;
                ">
                    <span style="font-size: 18px;">🔬</span>
                    <span>GPT-OSS 20B Model</span>
                </div>
                <div style="
                    display: flex;
                    align-items: center;
                    gap: 8px;
                    color: #3b82f6;
                    font-weight: 600;
                ">
                    <span style="font-size: 18px;">🧠</span>
                    <span>Thought Chain AI</span>
                </div>
                <div style="
                    display: flex;
                    align-items: center;
                    gap: 8px;
                    color: #f59e0b;
                    font-weight: 600;
                ">
                    <span style="font-size: 18px;">💻</span>
                    <span>Powered by Gradio</span>
                </div>
            </div>
            <div style="
                width: 80px;
                height: 2px;
                background: linear-gradient(45deg, #10b981, #3b82f6, #f59e0b);
                margin: 0 auto;
                border-radius: 1px;
            "></div>
        </div>
    """,
}
