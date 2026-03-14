# Hugging Face CORS Error - Solution Guide

## ❌ The Problem

When running the JeduAI app on web (Chrome/Edge), you're getting this error:

```
ClientException: Failed to fetch, uri=https://api-inference.huggingface.co/models/openai/whisper-large-v3
```

This is a **CORS (Cross-Origin Resource Sharing)** error. Web browsers block direct API calls to external services for security reasons.

## 🔍 Why This Happens

1. **Browser Security**: Web browsers prevent JavaScript from making direct requests to different domains
2. **Hugging Face API**: Doesn't allow direct calls from web browsers (only from servers)
3. **Web vs Mobile**: This error ONLY happens on web, not on mobile/desktop apps

## ✅ Solutions (Choose One)

### Solution 1: Run on Windows Desktop (RECOMMENDED - Easiest)

This bypasses the CORS issue completely because desktop apps don't have browser restrictions.

**Steps:**

1. Stop the current web app (press `q` in the terminal)
2. Run on Windows desktop instead:

```bash
flutter run -d windows
```

**Advantages:**
- ✅ No CORS issues
- ✅ Better performance
- ✅ Native Windows app
- ✅ Works immediately

---

### Solution 2: Use a Proxy Server (For Web Deployment)

Create a backend proxy server that forwards requests to Hugging Face.

**Steps:**

1. Create a simple Node.js proxy server
2. Deploy it (e.g., on Vercel, Netlify, or your own server)
3. Update the API calls to go through your proxy

**Example Proxy (Node.js):**

```javascript
// server.js
const express = require('express');
const cors = require('cors');
const axios = require('axios');

const app = express();
app.use(cors());
app.use(express.json());

const HF_TOKEN = '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';

app.post('/api/transcribe', async (req, res) => {
  try {
    const response = await axios.post(
      'https://api-inference.huggingface.co/models/openai/whisper-large-v3',
      req.body,
      {
        headers: {
          'Authorization': `Bearer ${HF_TOKEN}`,
          'Content-Type': 'application/octet-stream',
        },
      }
    );
    res.json(response.data);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.post('/api/translate', async (req, res) => {
  try {
    const response = await axios.post(
      'https://api-inference.huggingface.co/models/facebook/nllb-200-distilled-600M',
      req.body,
      {
        headers: {
          'Authorization': `Bearer ${HF_TOKEN}`,
          'Content-Type': 'application/json',
        },
      }
    );
    res.json(response.data);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.listen(3000, () => console.log('Proxy running on port 3000'));
```

Then update your Flutter code to use the proxy URL instead.

---

### Solution 3: Use Chrome with CORS Disabled (TESTING ONLY)

**⚠️ WARNING: Only for local testing, NOT for production!**

**Steps:**

1. Close all Chrome windows
2. Run Chrome with CORS disabled:

**Windows:**
```bash
"C:\Program Files\Google\Chrome\Application\chrome.exe" --disable-web-security --user-data-dir="C:\temp\chrome-dev"
```

3. Run your Flutter app:
```bash
flutter run -d chrome --web-browser-flag="--disable-web-security"
```

**Disadvantages:**
- ⚠️ Security risk
- ⚠️ Only works locally
- ⚠️ Not suitable for production

---

### Solution 4: Use Flutter Web with Backend API (Production)

Build a proper backend API using:
- Firebase Cloud Functions
- AWS Lambda
- Google Cloud Functions
- Your own server

**Architecture:**
```
Flutter Web App → Your Backend API → Hugging Face API
```

---

## 🎯 RECOMMENDED SOLUTION FOR YOU

**Run on Windows Desktop:**

```bash
# Stop the web app (press 'q' in terminal)
# Then run:
flutter run -d windows
```

This is the easiest and most reliable solution for testing the media translation module.

---

## 📱 Platform Comparison

| Platform | CORS Issue | Recommended |
|----------|------------|-------------|
| Windows Desktop | ❌ No | ✅ YES |
| Android | ❌ No | ✅ YES |
| iOS | ❌ No | ✅ YES |
| Web (Chrome/Edge) | ✅ Yes | ❌ Needs proxy |

---

## 🔧 Quick Fix Commands

### Stop Current Web App
```bash
# In the terminal where Flutter is running, press:
q
```

### Run on Windows Desktop
```bash
flutter run -d windows
```

### Check Available Devices
```bash
flutter devices
```

---

## 📝 Additional Notes

1. **Mobile Apps**: If you build for Android/iOS, there will be NO CORS issues
2. **Desktop Apps**: Windows/macOS/Linux apps don't have CORS restrictions
3. **Web Apps**: Always need a backend proxy for production

---

## 🎉 After Switching to Windows Desktop

Once you run on Windows desktop, you'll be able to:
- ✅ Upload audio/video files
- ✅ Get real transcriptions from Whisper
- ✅ Get real translations from NLLB
- ✅ Download all generated files
- ✅ No CORS errors!

---

## 🆘 Still Having Issues?

If you still face problems after switching to Windows desktop:

1. Check your internet connection
2. Verify Hugging Face token is valid
3. Check if Hugging Face API is accessible from your network
4. Try with a smaller file first (< 5MB)

---

## 📚 Learn More

- [CORS Explained](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
- [Flutter Web Limitations](https://docs.flutter.dev/platform-integration/web/faq)
- [Hugging Face API Docs](https://huggingface.co/docs/api-inference/index)
