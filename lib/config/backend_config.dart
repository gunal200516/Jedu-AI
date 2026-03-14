/// Backend API Configuration
/// 
/// Configuration for JeduAI backend server
library;

class BackendConfig {
  // Backend server URL
  // Change this to your deployed backend URL in production
  static const String baseUrl = 'http://localhost:8000';
  
  // API endpoints
  static const String mediaProcessEndpoint = '/api/media/process';
  static const String mediaDownloadEndpoint = '/api/media/download';
  static const String healthEndpoint = '/health';
  
  // Get full URL for media processing
  static String get mediaProcessUrl => '$baseUrl$mediaProcessEndpoint';
  
  // Get full URL for file download
  static String getDownloadUrl(String jobId, String filename) {
    return '$baseUrl$mediaDownloadEndpoint/$jobId/$filename';
  }
  
  // Get health check URL
  static String get healthUrl => '$baseUrl$healthEndpoint';
  
  // Timeout configuration
  static const int apiTimeout = 180; // 3 minutes for processing
  static const int downloadTimeout = 60; // 1 minute for downloads
}
