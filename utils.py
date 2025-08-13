# Utility functions
import os
from config import CSS_FILE_PATH


def load_css():
    """Load CSS file content"""
    try:
        if os.path.exists(CSS_FILE_PATH):
            with open(CSS_FILE_PATH, "r", encoding="utf-8") as f:
                return f.read()
        else:
            print(f"Warning: CSS file not found at {CSS_FILE_PATH}")
            return ""
    except Exception as e:
        print(f"Error loading CSS: {e}")
        return ""
