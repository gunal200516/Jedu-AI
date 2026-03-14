/// Groq API Configuration for Audio/Video Translation
///
/// SECURITY NOTE:
/// - This file contains API keys and should not be committed to Git
library;

class GroqConfig {
  // Groq API Key for audio and video translation
  static const String apiKey = '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';

  // API Endpoints
  static const String baseUrl = 'https://api.groq.com/openai/v1';
  
  // Audio transcription endpoint (Whisper model)
  static const String transcriptionEndpoint = '/audio/transcriptions';
  
  // Translation endpoint (using chat completions)
  static const String chatEndpoint = '/chat/completions';
  
  // Models
  static const String whisperModel = 'whisper-large-v3';
  static const String translationModel = 'llama-3.3-70b-versatile';
  
  // Get full API URLs
  static String get transcriptionUrl => '$baseUrl$transcriptionEndpoint';
  static String get chatUrl => '$baseUrl$chatEndpoint';
  
  // Headers for API requests
  static Map<String, String> get headers => {
    'Authorization': 'Bearer $apiKey',
    'Content-Type': 'application/json',
  };
  
  // Headers for multipart requests (audio upload)
  static Map<String, String> get multipartHeaders => {
    'Authorization': 'Bearer $apiKey',
  };
}
