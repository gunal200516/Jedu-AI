/// Gemini API Configuration
///
/// SECURITY NOTE:
/// - This file contains API keys and should not be committed to Git
/// - It's already in .gitignore
library;

class GeminiConfig {
  // Your Gemini API Key - Get it from https://makersuite.google.com/app/apikey
  static const String apiKey = 'YOUR_API_KEY_HERE';

  // API Endpoints - Using v1beta with gemini-2.5-flash
  static const String baseUrl =
      'https://generativelanguage.googleapis.com/v1beta';
  static const String modelName = 'gemini-2.5-flash';
  static const String translateEndpoint = '/models/$modelName:generateContent';

  // Project Details
  static const String projectName = 'projects/334561337628';
  static const String projectNumber = '334561337628';

  // Get full API URL
  static String get translateUrl => '$baseUrl$translateEndpoint?key=$apiKey';

  // AI Tutor URL (same API key)
  static String get aiTutorUrl => '$baseUrl$translateEndpoint?key=$apiKey';
}
