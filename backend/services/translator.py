# services/translator.py
from googletrans import Translator

def translate(text: str, source: str = "en", target: str = "en") -> str:
    """
    Translate text from source language to target language.
    Returns the translated text.
    If translation fails, returns the original text.
    """
    if source == target or not text:
        return text
    try:
        translator_instance = Translator()
        translated = translator_instance.translate(text, src=source, dest=target)
        return translated.text.strip()
    except Exception as e:
        print(f"Translation error: {e}")
        return text


