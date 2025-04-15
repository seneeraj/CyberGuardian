# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dlieeOEyCdgGnavJpgrYK4H5DmxuN-D6
"""

def get_ai_response(user_input):
    suspicious_phrases = ["urgent payment", "click here", "verify account", "free prize", "install now"]

    if not user_input.strip():
        return "⚠️ Please enter a valid message to analyze."

    lower_input = user_input.lower()

    if any(phrase in lower_input for phrase in suspicious_phrases):
        return "🚨 This message appears to be a scam. Please avoid interacting with it and report to CyberGuardian."
    else:
        return "✅ This message does not show clear signs of fraud. Stay alert and double-check the source."