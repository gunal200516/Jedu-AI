/// Hugging Face API Configuration for Audio/Video Translation
///
/// SECURITY NOTE:
/// - This file contains API keys and should not be committed to Git
library;

class HuggingFaceConfig {
  // Hugging Face API Token
  static const String apiToken = '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';

  // API Base URL
  static const String baseUrl = 'https://api-inference.huggingface.co';

  // Models
  // Seamless M4T V2 Large - Multilingual translation and speech
  static const String seamlessM4TModel = 'facebook/seamless-m4t-v2-large';
  
  // Whisper for speech-to-text
  static const String whisperModel = 'openai/whisper-large-v3';
  
  // API Endpoints
  static String get seamlessM4TUrl => '$baseUrl/models/$seamlessM4TModel';
  static String get whisperUrl => '$baseUrl/models/$whisperModel';

  // Headers for API requests
  static Map<String, String> get headers => {
        'Authorization': 'Bearer $apiToken',
        'Content-Type': 'application/json',
      };

  // Headers for audio file upload
  static Map<String, String> get audioHeaders => {
        'Authorization': 'Bearer $apiToken',
      };

  // Supported language codes for Seamless M4T
  static const Map<String, String> languageCodes = {
    'English': 'eng',
    'Hindi': 'hin',
    'Tamil': 'tam',
    'Telugu': 'tel',
    'Malayalam': 'mal',
    'Bengali': 'ben',
    'Kannada': 'kan',
    'Marathi': 'mar',
    'Gujarati': 'guj',
    'Punjabi': 'pan',
    'Urdu': 'urd',
    'Spanish': 'spa',
    'French': 'fra',
    'German': 'deu',
    'Chinese': 'cmn',
    'Japanese': 'jpn',
    'Korean': 'kor',
    'Arabic': 'arb',
    'Russian': 'rus',
    'Portuguese': 'por',
    'Italian': 'ita',
    'Dutch': 'nld',
    'Turkish': 'tur',
    'Polish': 'pol',
    'Vietnamese': 'vie',
    'Thai': 'tha',
    'Indonesian': 'ind',
  };

  // Get language code for Seamless M4T
  static String getLanguageCode(String language) {
    return languageCodes[language] ?? 'eng';
  }
}
