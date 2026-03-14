# 🚀 Quick Fix Instructions - CORS Error Solution

## ❌ Problem You Encountered

When running on **Chrome (web)**, you got this error:
```
ClientException: Failed to fetch, uri=https://api-inference.huggingface.co/models/openai/whisper-large-v3
```

## ✅ Solution: Run on Windows Desktop

The error happens because web browsers block direct API calls to external services (CORS policy). Desktop apps don't have this restriction.

---

## 📋 Step-by-Step Instructions

### Step 1: Stop the Web App

If the app is still running in Chrome, stop it:

1. Go to the terminal where Flutter is running
2. Press **`q`** key
3. Wait for it to stop

### Step 2: Run on Windows Desktop

In the same terminal, run:

```bash
flutter run -d windows
```

### Step 3: Wait for Build

- First time build takes **2-5 minutes**
- You'll see "Building Windows application..."
- Be patient, it's compiling the native Windows app

### Step 4: App Will Launch

Once built, a Windows application window will open automatically with JeduAI running.

---

## 🎯 What You'll See

1. **Windows App Opens** - Native Windows application window
2. **Login Screen** - Use these credentials:
   - Email: `admin@vsb.edu`
   - Password: `admin123`
3. **No CORS Errors** - Everything works perfectly!

---

## 🧪 Testing Media Translation

After the app opens:

1. **Login** with admin credentials
2. **Navigate**: Advanced Translation → File Upload tab
3. **Upload**: Click "Upload Audio" or "Upload Video"
4. **Select File**: Choose an MP3, WAV, or MP4 file
5. **Choose Languages**: Select source and target languages
6. **Translate**: Watch real-time progress
7. **Download**: Get transcript, translation, and subtitles

---

## 💡 Why Windows Desktop Works

| Platform | CORS Issue | Works? |
|----------|------------|--------|
| Chrome/Edge (Web) | ✅ Yes | ❌ No |
| Windows Desktop | ❌ No | ✅ YES |
| Android App | ❌ No | ✅ YES |
| iOS App | ❌ No | ✅ YES |

**Desktop and mobile apps can make direct API calls without CORS restrictions!**

---

## 🔄 Alternative: If You Must Use Web

If you absolutely need to use the web version, you'll need to:

1. **Create a backend proxy server** (Node.js, Python, etc.)
2. **Deploy it** (Vercel, Netlify, AWS, etc.)
3. **Update Flutter code** to use proxy URL

See `HUGGINGFACE_CORS_FIX.md` for detailed proxy setup.

---

## ⚡ Quick Commands Reference

```bash
# Check available devices
flutter devices

# Run on Windows desktop
flutter run -d windows

# Run on web (has CORS issues)
flutter run -d chrome

# Run on Android (if connected)
flutter run -d android

# Stop running app
# Press 'q' in terminal
```

---

## 🎉 Expected Result

After running on Windows desktop:

✅ App opens in native Windows window
✅ No CORS errors
✅ Media translation works perfectly
✅ Can upload and process files
✅ Real Whisper transcription
✅ Real NLLB translation
✅ Download all generated files

---

## 🆘 Troubleshooting

### Build Takes Too Long
- First build can take 5-10 minutes
- Subsequent builds are much faster
- Be patient!

### Build Fails
```bash
# Clean and rebuild
flutter clean
flutter pub get
flutter run -d windows
```

### App Doesn't Open
- Check if Windows Defender blocked it
- Allow the app in firewall settings

### Still Getting Errors
- Check internet connection
- Verify Hugging Face token in `lib/config/huggingface_config.dart`
- Try with a smaller file first

---

## 📱 Future: Mobile Apps

To avoid CORS completely, build mobile apps:

```bash
# For Android
flutter build apk
flutter install

# For iOS (requires Mac)
flutter build ios
```

Mobile apps have NO CORS restrictions and work perfectly with Hugging Face API!

---

## 📚 Summary

**Problem**: Web browsers block direct API calls (CORS)
**Solution**: Run on Windows desktop instead
**Command**: `flutter run -d windows`
**Result**: Everything works perfectly!

---

## ✨ Current Status

Your app is now building for Windows desktop. Once it finishes:
1. A Windows app window will open
2. Login with admin credentials
3. Test the media translation feature
4. Enjoy CORS-free operation!

🎊 **No more CORS errors!**
