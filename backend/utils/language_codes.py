"""
Language code mappings for Whisper and NLLB models
"""

# Whisper language codes (ISO 639-1)
WHISPER_LANGUAGE_CODES = {
    'English': 'en',
    'Tamil': 'ta',
    'Hindi': 'hi',
    'Telugu': 'te',
    'Kannada': 'kn',
    'Malayalam': 'ml',
    'Bengali': 'bn',
    'Marathi': 'mr',
    'Gujarati': 'gu',
    'Punjabi': 'pa',
    'Urdu': 'ur',
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
    'Chinese': 'zh',
    'Japanese': 'ja',
    'Korean': 'ko',
    'Arabic': 'ar',
    'Russian': 'ru',
    'Portuguese': 'pt',
    'Italian': 'it',
    'Dutch': 'nl',
    'Turkish': 'tr',
    'Polish': 'pl',
    'Vietnamese': 'vi',
    'Thai': 'th',
    'Indonesian': 'id',
}

# NLLB-200 language codes (3-letter codes with script)
NLLB_LANGUAGE_CODES = {
    'English': 'eng_Latn',
    'Tamil': 'tam_Taml',
    'Hindi': 'hin_Deva',
    'Telugu': 'tel_Telu',
    'Kannada': 'kan_Knda',
    'Malayalam': 'mal_Mlym',
    'Bengali': 'ben_Beng',
    'Marathi': 'mar_Deva',
    'Gujarati': 'guj_Gujr',
    'Punjabi': 'pan_Guru',
    'Urdu': 'urd_Arab',
    'Spanish': 'spa_Latn',
    'French': 'fra_Latn',
    'German': 'deu_Latn',
    'Chinese': 'zho_Hans',
    'Japanese': 'jpn_Jpan',
    'Korean': 'kor_Hang',
    'Arabic': 'arb_Arab',
    'Russian': 'rus_Cyrl',
    'Portuguese': 'por_Latn',
    'Italian': 'ita_Latn',
    'Dutch': 'nld_Latn',
    'Turkish': 'tur_Latn',
    'Polish': 'pol_Latn',
    'Vietnamese': 'vie_Latn',
    'Thai': 'tha_Thai',
    'Indonesian': 'ind_Latn',
}


def get_whisper_code(language: str) -> str:
    """Get Whisper language code"""
    return WHISPER_LANGUAGE_CODES.get(language, 'en')


def get_nllb_code(language: str) -> str:
    """Get NLLB language code"""
    return NLLB_LANGUAGE_CODES.get(language, 'eng_Latn')
