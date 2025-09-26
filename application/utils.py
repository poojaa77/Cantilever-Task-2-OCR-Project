# pip install googletrans==4.0.0rc1
from googletrans import Translator
import time
import random

translator = Translator()

def detect_language(text):
    """Detect language with error handling"""
    try:
        # Check if text is valid
        if not text or not isinstance(text, str) or len(text.strip()) == 0:
            print("Warning: Empty or invalid text for language detection")
            return 'en', 0.0
        
        # Clean the text
        cleaned_text = text.strip()
        
        # If text is too short, default to English
        if len(cleaned_text) < 3:
            print("Warning: Text too short for language detection")
            return 'en', 0.0
        
        # Add retry mechanism for Google Translate API
        max_retries = 3
        for attempt in range(max_retries):
            try:
                # Add small delay to avoid rate limiting
                if attempt > 0:
                    time.sleep(random.uniform(1, 3))
                
                detected_lang_data = translator.detect(cleaned_text)
                
                if detected_lang_data and hasattr(detected_lang_data, 'lang'):
                    lang = detected_lang_data.lang
                    conf = getattr(detected_lang_data, 'confidence', 0.0)
                    print(f"Detected language: {lang} (confidence: {conf})")
                    return lang, conf
                else:
                    print("Warning: Invalid detection result")
                    return 'en', 0.0
                    
            except Exception as api_error:
                print(f"Language detection attempt {attempt + 1} failed: {api_error}")
                if attempt == max_retries - 1:
                    print("All language detection attempts failed, defaulting to English")
                    return 'en', 0.0
                continue
                
    except Exception as e:
        print(f"Language detection error: {e}")
        return 'en', 0.0

def translate_text(text, dest):
    """Translate text with error handling"""
    try:
        # Validate input
        if not text or not isinstance(text, str) or len(text.strip()) == 0:
            print("Warning: Empty or invalid text for translation")
            return "No text to translate"
        
        if not dest:
            dest = 'en'
        
        cleaned_text = text.strip()
        
        # Check if text is already in target language
        current_lang, _ = detect_language(cleaned_text)
        if current_lang == dest:
            print(f"Text is already in target language ({dest})")
            return cleaned_text
        
        # Add retry mechanism for translation
        max_retries = 3
        for attempt in range(max_retries):
            try:
                # Add small delay to avoid rate limiting
                if attempt > 0:
                    time.sleep(random.uniform(1, 3))
                
                translated_text = translator.translate(cleaned_text, dest=dest)
                
                if translated_text and hasattr(translated_text, 'text'):
                    result = translated_text.text
                    print(f"Translation successful: {cleaned_text[:50]}... -> {result[:50]}...")
                    return result
                else:
                    print("Warning: Invalid translation result")
                    return cleaned_text
                    
            except Exception as api_error:
                print(f"Translation attempt {attempt + 1} failed: {api_error}")
                if attempt == max_retries - 1:
                    print("All translation attempts failed, returning original text")
                    return cleaned_text
                continue
                
    except Exception as e:
        print(f"Translation error: {e}")
        return text if text else "Translation failed"


languages = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'he': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'or': 'odia',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'ug': 'uyghur',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
}