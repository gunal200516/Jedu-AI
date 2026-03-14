# Media Translation Module - Quick Reference

## 🚀 Quick Start

```bash
flutter pub get
flutter run -d chrome
# Navigate to: Advanced Translation → File Upload
```

## 📁 Module Location

```
lib/modules/media_translation/
```

## 🔑 Key Files

| File | Purpose |
|------|---------|
| `media_translation_job.dart` | Job model |
| `hf_media_translation_api.dart` | Hugging Face API |
| `media_translation_orchestrator.dart` | Workflow |
| `media_translation_controller.dart` | State management |
| `media_translation_module_view.dart` | Main UI |

## 🎯 API Endpoints

```dart
// Transcription
POST https://api-inference.huggingface.co/models/openai/whisper-large-v3

// Translation
POST https://api-inference.huggingface.co/models/facebook/nllb-200-distilled-600M
```

## 🔐 Configuration

```dart
// lib/config/huggingface_config.dart
static const String apiToken = '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';
```

## 📝 Usage Example

```dart
// Get controller
final controller = Get.put(MediaTranslationController());

// Start translation
await controller.startTranslation(
  fileName: 'audio.mp3',
  fileBytes: fileBytes,
  fileSize: fileSize,
  sourceLanguage: 'English',
  targetLanguage: 'Tamil',
);

// Monitor progress
Obx(() {
  final job = controller.currentJob.value;
  print('Status: ${job?.statusText}');
  print('Progress: ${job?.progress}');
});
```

## 🌍 Supported Languages

English, Tamil, Hindi, Telugu, Kannada, Malayalam, Bengali, Marathi, Gujarati, Punjabi, Urdu, Spanish, French, German, Chinese, Japanese, Korean, Arabic, Russian, Portuguese, Italian, Dutch, Turkish, Polish, Vietnamese, Thai, Indonesian

## 📦 Supported Formats

**Audio**: MP3, WAV, M4A, OGG, FLAC, AAC
**Video**: MP4, MOV, MKV, WEBM, AVI

## 📏 Size Limits

- Audio: 25 MB
- Video: 100 MB

## 📤 Output Files

- ✅ Transcript TXT
- ✅ Translation TXT
- ✅ Subtitle SRT (video only)
- ❌ Translated Audio (not available)
- ❌ Video Package (not available)

## 🔄 Workflow Steps

1. **Uploading** (10%)
2. **Extracting Audio** (20%)
3. **Transcribing** (40%)
4. **Translating** (70%)
5. **Generating Files** (90%)
6. **Completed** (100%)

## ⚠️ Error Codes

| Code | Meaning | Action |
|------|---------|--------|
| 200 | Success | Continue |
| 429 | Rate limited | Retry with backoff |
| 503 | Model loading | Wait and retry |
| Timeout | Request timeout | Retry |

## 🐛 Debugging

```dart
// Check console for:
🎤 Transcribing audio: filename.mp3
✅ Transcription successful
🌐 Translating text
✅ Translation successful
```

## 🧪 Testing

```dart
// Test audio
controller.startTranslation(
  fileName: 'test.mp3',
  fileBytes: audioBytes,
  fileSize: 1024000,
  sourceLanguage: 'English',
  targetLanguage: 'Tamil',
);

// Verify output
expect(job.transcriptText, isNotNull);
expect(job.translatedText, isNotNull);
expect(job.status, JobStatus.completed);
```

## 📊 Performance

- First translation: 20-30s
- Subsequent: 10-20s
- Timeout: 120s
- Max retries: 3

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| Model loading | Wait 10-20s, retry |
| Rate limited | Wait, automatic retry |
| Invalid token | Check config file |
| File too large | Reduce file size |
| Unsupported format | Use supported format |

## 📚 Documentation

- `NEW_MEDIA_TRANSLATION_MODULE.md` - Full docs
- `IMPLEMENTATION_STEPS.md` - Setup guide
- `MEDIA_TRANSLATION_COMPLETE.md` - Summary

## 🎨 UI Components

```dart
// Upload card
UploadCard(
  title: 'Upload Audio',
  subtitle: 'MP3, WAV, M4A',
  icon: Icons.audiotrack,
  color: Colors.purple,
  onTap: () => pickFile(),
)

// Status card
JobStatusCard(job: currentJob)

// Transcript panel
TranscriptPanel(
  title: 'Transcript',
  content: transcriptText,
  color: Colors.blue,
)

// Download section
DownloadSection(job: completedJob)
```

## 🔗 Integration

```dart
// In advanced_translation_view.dart
import '../../modules/media_translation/presentation/views/media_translation_module_view.dart';

// Use in TabBarView
const MediaTranslationModuleView()
```

## 🚫 Old Files (Deprecated)

- `lib/services/media_translation_service.dart`
- `lib/services/real_time_translation_service.dart`
- `lib/services/real_video_translation_service.dart`
- `lib/services/video_translation_pipeline_service.dart`
- `lib/views/student/media_translation_view.dart`

**Do not use these for new development!**

## ✅ Checklist

- [ ] HF token configured
- [ ] Dependencies installed
- [ ] App runs without errors
- [ ] Audio translation works
- [ ] Video translation works
- [ ] Downloads work
- [ ] Error handling works

## 🎯 Success Metrics

- Real transcription (not fake)
- Accurate translation
- Downloadable files
- Clear error messages
- < 30s processing time

## 📞 Support

Check console logs for detailed error messages. All API calls are logged with 🎤, 🌐, ✅, and ❌ emojis.

---

**Quick Tip**: First translation may take longer due to model warm-up. Subsequent translations are faster!
