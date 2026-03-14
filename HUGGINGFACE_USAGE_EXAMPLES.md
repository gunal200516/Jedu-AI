# Hugging Face Translation - Usage Examples

## Quick Start

### 1. Basic Text Translation

```dart
import 'package:get/get.dart';
import 'services/huggingface_translation_service.dart';

// Get the service instance
final hfService = Get.find<HuggingFaceTranslationService>();

// Translate text
final result = await hfService.translateText(
  text: 'Welcome to JeduAI. Today we will learn about artificial intelligence.',
  sourceLanguage: 'English',
  targetLanguage: 'Hindi',
);

if (result.success) {
  print('Original: ${result.originalText}');
  print('Translated: ${result.translatedText}');
  // Output: "जेडुएआई में आपका स्वागत है। आज हम कृत्रिम बुद्धिमत्ता के बारे में सीखेंगे।"
} else {
  print('Error: ${result.error}');
}
```

### 2. Audio Transcription

```dart
import 'dart:io';

// Transcribe audio file
final audioFile = File('path/to/lecture.mp3');

final result = await hfService.transcribeAudio(
  audioFile: audioFile,
  language: 'English',
);

if (result.success) {
  print('Transcription: ${result.transcription}');
} else {
  print('Error: ${result.error}');
}
```

### 3. Audio Translation (Transcribe + Translate)

```dart
// Translate audio from English to Tamil
final result = await hfService.translateAudio(
  audioFile: File('path/to/english_lecture.mp3'),
  sourceLanguage: 'English',
  targetLanguage: 'Tamil',
);

if (result.success) {
  print('Original (English): ${result.originalText}');
  print('Translated (Tamil): ${result.translatedText}');
}
```

### 4. Video Translation with Subtitles

```dart
// Translate video and generate subtitles
final result = await hfService.translateVideo(
  videoFile: File('path/to/lesson.mp4'),
  sourceLanguage: 'English',
  targetLanguage: 'Hindi',
  videoDuration: Duration(minutes: 10),
);

if (result.success) {
  print('Generated ${result.subtitles.length} subtitle segments');
  
  // Export subtitles as SRT file
  final srtContent = result.subtitles.map((s) => s.toSRT()).join('\n');
  await File('subtitles.srt').writeAsString(srtContent);
  
  // Display subtitles
  for (var subtitle in result.subtitles) {
    print('${subtitle.startTime} - ${subtitle.endTime}: ${subtitle.text}');
  }
}
```

### 5. Batch Translation

```dart
// Translate multiple texts at once
final lessonContent = [
  'Introduction to Machine Learning',
  'What is supervised learning?',
  'Understanding neural networks',
  'Applications of AI in education',
];

final results = await hfService.batchTranslate(
  texts: lessonContent,
  sourceLanguage: 'English',
  targetLanguage: 'Telugu',
);

for (int i = 0; i < results.length; i++) {
  if (results[i].success) {
    print('${i + 1}. ${results[i].translatedText}');
  }
}
```

## UI Integration Examples

### 6. Translation with Progress Indicator

```dart
class TranslationWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final hfService = Get.find<HuggingFaceTranslationService>();
    
    return Obx(() {
      if (hfService.isProcessing.value) {
        return Column(
          children: [
            CircularProgressIndicator(
              value: hfService.progress.value,
            ),
            SizedBox(height: 8),
            Text(hfService.currentStep.value),
          ],
        );
      }
      
      return ElevatedButton(
        onPressed: () async {
          await hfService.translateAudio(
            audioFile: selectedFile,
            sourceLanguage: 'English',
            targetLanguage: 'Hindi',
          );
        },
        child: Text('Translate Audio'),
      );
    });
  }
}
```

### 7. Real-time Translation for Live Classes

```dart
class LiveClassTranslation {
  final hfService = Get.find<HuggingFaceTranslationService>();
  
  // Buffer for collecting audio chunks
  List<int> audioBuffer = [];
  
  Future<void> translateLiveAudio(List<int> audioChunk) async {
    // Add chunk to buffer
    audioBuffer.addAll(audioChunk);
    
    // When buffer reaches threshold (e.g., 5 seconds of audio)
    if (audioBuffer.length >= 5 * 16000) { // 5 seconds at 16kHz
      // Save buffer to temp file
      final tempFile = File('temp_audio.wav');
      await tempFile.writeAsBytes(audioBuffer);
      
      // Transcribe and translate
      final result = await hfService.translateAudio(
        audioFile: tempFile,
        sourceLanguage: 'English',
        targetLanguage: studentLanguage,
      );
      
      if (result.success) {
        // Display translation to student
        displaySubtitle(result.translatedText);
      }
      
      // Clear buffer
      audioBuffer.clear();
      
      // Clean up temp file
      await tempFile.delete();
    }
  }
  
  void displaySubtitle(String text) {
    // Show subtitle on screen
    Get.snackbar('Translation', text);
  }
}
```

### 8. Offline Translation Cache

```dart
import 'package:shared_preferences/shared_preferences.dart';

class CachedTranslationService {
  final hfService = Get.find<HuggingFaceTranslationService>();
  
  Future<String> translateWithCache({
    required String text,
    required String sourceLanguage,
    required String targetLanguage,
  }) async {
    final prefs = await SharedPreferences.getInstance();
    final cacheKey = '${text}_${sourceLanguage}_${targetLanguage}';
    
    // Check cache first
    final cached = prefs.getString(cacheKey);
    if (cached != null) {
      print('✅ Using cached translation');
      return cached;
    }
    
    // Translate using Hugging Face
    final result = await hfService.translateText(
      text: text,
      sourceLanguage: sourceLanguage,
      targetLanguage: targetLanguage,
    );
    
    if (result.success) {
      // Save to cache
      await prefs.setString(cacheKey, result.translatedText);
      return result.translatedText;
    }
    
    return text; // Return original on error
  }
}
```

### 9. Multi-Language Subtitle Generator

```dart
class MultiLanguageSubtitles {
  final hfService = Get.find<HuggingFaceTranslationService>();
  
  Future<Map<String, List<SubtitleSegment>>> generateMultiLanguageSubtitles({
    required File videoFile,
    required String sourceLanguage,
    required List<String> targetLanguages,
    required Duration videoDuration,
  }) async {
    final subtitles = <String, List<SubtitleSegment>>{};
    
    // First, transcribe the video
    final transcription = await hfService.transcribeAudio(
      audioFile: videoFile,
      language: sourceLanguage,
    );
    
    if (!transcription.success) {
      return subtitles;
    }
    
    // Generate subtitles for each target language
    for (var targetLang in targetLanguages) {
      final result = await hfService.translateVideo(
        videoFile: videoFile,
        sourceLanguage: sourceLanguage,
        targetLanguage: targetLang,
        videoDuration: videoDuration,
      );
      
      if (result.success) {
        subtitles[targetLang] = result.subtitles;
      }
    }
    
    return subtitles;
  }
  
  Future<void> exportSubtitles(
    Map<String, List<SubtitleSegment>> subtitles,
    String videoName,
  ) async {
    for (var entry in subtitles.entries) {
      final language = entry.key;
      final segments = entry.value;
      
      final srtContent = segments.map((s) => s.toSRT()).join('\n');
      final fileName = '${videoName}_${language}.srt';
      
      await File(fileName).writeAsString(srtContent);
      print('✅ Exported: $fileName');
    }
  }
}
```

### 10. Assessment Translation

```dart
class AssessmentTranslator {
  final hfService = Get.find<HuggingFaceTranslationService>();
  
  Future<Map<String, dynamic>> translateAssessment({
    required Map<String, dynamic> assessment,
    required String targetLanguage,
  }) async {
    final translatedAssessment = Map<String, dynamic>.from(assessment);
    
    // Translate title
    final titleResult = await hfService.translateText(
      text: assessment['title'],
      sourceLanguage: 'English',
      targetLanguage: targetLanguage,
    );
    translatedAssessment['title'] = titleResult.translatedText;
    
    // Translate description
    final descResult = await hfService.translateText(
      text: assessment['description'],
      sourceLanguage: 'English',
      targetLanguage: targetLanguage,
    );
    translatedAssessment['description'] = descResult.translatedText;
    
    // Translate questions
    final questions = assessment['questions'] as List;
    final translatedQuestions = [];
    
    for (var question in questions) {
      final qResult = await hfService.translateText(
        text: question['question'],
        sourceLanguage: 'English',
        targetLanguage: targetLanguage,
      );
      
      // Translate options
      final options = question['options'] as List;
      final translatedOptions = [];
      
      for (var option in options) {
        final oResult = await hfService.translateText(
          text: option,
          sourceLanguage: 'English',
          targetLanguage: targetLanguage,
        );
        translatedOptions.add(oResult.translatedText);
      }
      
      translatedQuestions.add({
        'question': qResult.translatedText,
        'options': translatedOptions,
        'correctAnswer': question['correctAnswer'],
      });
    }
    
    translatedAssessment['questions'] = translatedQuestions;
    return translatedAssessment;
  }
}
```

## Error Handling Best Practices

```dart
class RobustTranslation {
  final hfService = Get.find<HuggingFaceTranslationService>();
  
  Future<String> translateWithFallback({
    required String text,
    required String sourceLanguage,
    required String targetLanguage,
  }) async {
    try {
      // Try Hugging Face first
      final result = await hfService.translateText(
        text: text,
        sourceLanguage: sourceLanguage,
        targetLanguage: targetLanguage,
      );
      
      if (result.success) {
        return result.translatedText;
      }
      
      // If Hugging Face fails, try Groq
      final groqService = Get.find<GroqAudioTranslationService>();
      // ... use Groq as fallback
      
    } catch (e) {
      print('Translation error: $e');
      
      // Show user-friendly error
      Get.snackbar(
        'Translation Error',
        'Unable to translate. Please check your internet connection.',
        snackPosition: SnackPosition.BOTTOM,
      );
      
      // Return original text
      return text;
    }
    
    return text;
  }
}
```

## Performance Tips

1. **Warm up the model on app start** (already done in main.dart)
2. **Cache frequently translated content**
3. **Use batch translation for multiple texts**
4. **Implement request queuing to avoid rate limits**
5. **Show progress indicators for long operations**
6. **Handle 503 errors gracefully (model loading)**

## Language Code Reference

```dart
// Common language codes for Seamless M4T
final languageCodes = {
  'English': 'eng',
  'Hindi': 'hin',
  'Tamil': 'tam',
  'Telugu': 'tel',
  'Malayalam': 'mal',
  'Bengali': 'ben',
  'Kannada': 'kan',
  'Marathi': 'mar',
  'Spanish': 'spa',
  'French': 'fra',
  'German': 'deu',
  'Chinese': 'cmn',
  'Japanese': 'jpn',
  'Korean': 'kor',
  'Arabic': 'arb',
};
```

## Testing Checklist

- [ ] Test text translation with various languages
- [ ] Test audio transcription with different audio formats
- [ ] Test video translation with subtitle generation
- [ ] Test batch translation performance
- [ ] Test error handling (network errors, invalid files)
- [ ] Test model loading (503 error handling)
- [ ] Test with real classroom content
- [ ] Verify translation accuracy for educational terms
- [ ] Test caching mechanism
- [ ] Test UI responsiveness during translation

## Support

For issues or questions:
1. Check Hugging Face API status: https://status.huggingface.co
2. Review model documentation: https://huggingface.co/facebook/seamless-m4t-v2-large
3. Check API token validity
4. Verify internet connection
5. Review error logs in console
