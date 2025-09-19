# services/emergency.py
def check_emergency(text):
    """
    Very basic emergency detection.
    Returns severity: 'low' or 'high'.
    """
    emergency_keywords = [
        "chest pain", "shortness of breath", "severe bleeding",
        "unconscious", "severe headache", "heart attack", "stroke"
    ]
    text_lower = text.lower()
    for word in emergency_keywords:
        if word in text_lower:
            return {"severity": "high", "keyword": word}
    return {"severity": "low"}

