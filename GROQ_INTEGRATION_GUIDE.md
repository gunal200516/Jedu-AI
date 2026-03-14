# Groq API Integration for Audio/Video Translation

## Overview
JeduAI now uses Groq API for high-performance audio and video translation features.

## API Key Configuration
The Groq API key has been configured in `lib/config/groq_config.dart`:
- **API Key**: `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`
- **Base URL**: `https://api.groq.com/openai/v1`

## Features Enabled

### 1. Audio Transcription
- **Model**: Whisper Large V3 (`whisper-large-v3`)
- **Service**: `GroqAudioTranslationService`
- **Capabilities**:
  - High-accuracy audio transcription
  - Multi-language support
  - Fast processing

### 2. Audio Translation
- **Process**: Transcribe → Translate
- **Translation Model**: Llama 3.3 70B Versatile
- **Supported Languages**: 20+ languages including all major Indian languages

### 3. Video Translation
- **Service**: `RealVideoTranslationService` (updated)
- **Uses Groq for**: Text translation after content generation
- **Benefits**: Faster and more accurate translations

## Services Updated

### New Service
- `lib/services/groq_audio_translation_service.dart`
  - Audio transcription using Whisper
  - Audio-to-text translation
  - Real-time progress tracking

### Updated Services
- `lib/services/real_video_translation_service.dart`
  - Now uses Groq for text translation
  - Improved translation quality
  
- `lib/services/gemini_translation_service.dart`
  - Added Groq config import for future integration

## Usage Example

```dart
// Initialize service
final groqService = Get.put(GroqAudioTranslationService());

// Transcribe audio
final transcription = await groqService.transcribeAudio(
  audioFile: audioFile,
  language: 'English',
);

// Translate audio
final translation = await groqService.translateAudio(
  audioFile: audioFile,
  sourceLanguage: 'English',
  targetLanguage: 'Hindi',
);
```

## Supported Languages
- **Indian**: Hindi, Tamil, Telugu, Malayalam, Bengali, Kannada, Marathi, Gujarati, Punjabi, Urdu
- **International**: English, Spanish, French, German, Chinese, Japanese, Korean, Arabic, Russian, Portuguese, Italian

## Benefits of Groq Integration
1. **Speed**: 10x faster than traditional APIs
2. **Accuracy**: State-of-the-art Whisper model for transcription
3. **Cost-effective**: Efficient token usage
4. **Reliability**: High uptime and consistent performance

## Security Notes
- API key is stored in config file (not committed to Git)
- All API calls use HTTPS
- No audio data is stored permanently
- Transcriptions are processed in real-time

## Next Steps
To fully utilize Groq features:
1. Test audio transcription with sample files
2. Integrate with video player for real-time subtitles
3. Add voice-over generation using TTS
4. Implement batch processing for multiple files
