
import re

def check_link_safety(url: str) -> dict:
    suspicious_keywords = ["free", "win", "urgent", "login", "verify", "account", "gift"]
    is_suspicious = any(keyword in url.lower() for keyword in suspicious_keywords)

    if not url.startswith("http"):
        return {
            "verdict": "⚠️ Suspicious",
            "reason": "URL doesn't start with http or https"
        }
    elif is_suspicious:
        return {
            "verdict": "⚠️ Suspicious",
            "reason": "Contains phishing-related keywords"
        }
    elif re.match(r"https?://[a-zA-Z0-9.-]+\.[a-z]{2,}", url):
        return {
            "verdict": "✅ Safe",
            "reason": "URL pattern appears normal"
        }
    else:
        return {
            "verdict": "⚠️ Suspicious",
            "reason": "URL format not recognized"
        }
