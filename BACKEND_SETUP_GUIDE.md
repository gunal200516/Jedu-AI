## 🚀 JeduAI Backend Setup Guide

Complete guide to set up and run the FastAPI backend server for media translation.

---

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

---

## 🔧 Installation Steps

### Step 1: Navigate to Backend Directory

```bash
cd backend
```

### Step 2: Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- FastAPI - Web framework
- Uvicorn - ASGI server
- httpx - Async HTTP client
- python-multipart - File upload support
- python-dotenv - Environment variables
- pydantic - Data validation

---

## ⚙️ Configuration

### Step 1: Copy Environment File

```bash
copy .env.example .env
```

### Step 2: Edit `.env` File

The `.env` file is already configured with the Hugging Face token:

```env
HUGGINGFACE_API_TOKEN=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
HOST=0.0.0.0
PORT=8000
CORS_ORIGINS=http://localhost:*,http://127.0.0.1:*
MAX_AUDIO_SIZE_MB=25
MAX_VIDEO_SIZE_MB=100
UPLOAD_DIR=./uploads
TEMP_DIR=./temp
```

**Note**: The token is already set. No changes needed unless you want to use your own token.

---

## 🚀 Running the Backend

### Start the Server

```bash
python main.py
```

Or using uvicorn directly:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Expected Output

```
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

---

## ✅ Verify Backend is Running

### Method 1: Browser

Open your browser and go to:
```
http://localhost:8000
```

You should see:
```json
{
  "status": "healthy",
  "message": "JeduAI Media Translation Backend is running",
  "hf_token_configured": true
}
```

### Method 2: API Documentation

FastAPI provides automatic API documentation:
```
http://localhost:8000/docs
```

This shows all available endpoints with interactive testing.

### Method 3: Command Line

```bash
curl http://localhost:8000/health
```

---

## 📡 API Endpoints

### 1. Health Check
```
GET /health
```

Response:
```json
{
  "status": "healthy",
  "message": "Service is operational",
  "hf_token_configured": true
}
```

### 2. Process Media
```
POST /api/media/process
```

Request (multipart/form-data):
- `file`: Audio/video file
- `sourceLanguage`: Source language name (e.g., "English")
- `targetLanguage`: Target language name (e.g., "Tamil")
- `mediaType`: "audio" or "video"

Response:
```json
{
  "success": true,
  "jobId": "uuid-here",
  "transcript": "Transcribed text...",
  "translation": "Translated text...",
  "subtitleContent": "SRT content...",
  "downloads": {
    "transcriptTxt": "/api/media/download/uuid/transcript.txt",
    "translationTxt": "/api/media/download/uuid/translation.txt",
    "subtitleSrt": "/api/media/download/uuid/subtitles.srt",
    "translatedAudio": null,
    "processedVideo": null
  },
  "status": "completed"
}
```

### 3. Download File
```
GET /api/media/download/{job_id}/{filename}
```

Downloads generated files:
- `transcript.txt`
- `translation.txt`
- `subtitles.srt`

---

## 🧪 Testing the Backend

### Using curl

**Upload and process audio:**
```bash
curl -X POST http://localhost:8000/api/media/process \
  -F "file=@test_audio.mp3" \
  -F "sourceLanguage=English" \
  -F "targetLanguage=Tamil" \
  -F "mediaType=audio"
```

**Download transcript:**
```bash
curl http://localhost:8000/api/media/download/{job_id}/transcript.txt
```

### Using Python

```python
import requests

# Process media
with open('test_audio.mp3', 'rb') as f:
    files = {'file': f}
    data = {
        'sourceLanguage': 'English',
        'targetLanguage': 'Tamil',
        'mediaType': 'audio'
    }
    response = requests.post(
        'http://localhost:8000/api/media/process',
        files=files,
        data=data
    )
    result = response.json()
    print(result)
```

---

## 📁 Directory Structure

```
backend/
├── main.py                      # FastAPI application entry point
├── requirements.txt             # Python dependencies
├── .env                         # Environment configuration
├── .env.example                 # Example environment file
├── models/
│   └── schemas.py              # Pydantic models
├── routes/
│   └── media_translation.py    # API routes
├── services/
│   ├── hf_client.py            # Hugging Face API client
│   └── media_processor.py      # Media processing logic
├── utils/
│   ├── language_codes.py       # Language code mappings
│   └── subtitle_generator.py  # SRT subtitle generation
└── uploads/                     # Generated files (created automatically)
```

---

## 🔒 Security Notes

### Production Deployment

1. **Environment Variables**: Move sensitive data to secure environment variables
2. **CORS**: Update `CORS_ORIGINS` to specific domains
3. **HTTPS**: Use HTTPS in production
4. **Rate Limiting**: Add rate limiting middleware
5. **Authentication**: Add API key authentication if needed

### Example Production `.env`

```env
HUGGINGFACE_API_TOKEN=your_production_token
HOST=0.0.0.0
PORT=8000
CORS_ORIGINS=https://yourdomain.com
MAX_AUDIO_SIZE_MB=25
MAX_VIDEO_SIZE_MB=100
```

---

## 🐛 Troubleshooting

### Issue: "Module not found"

**Solution**: Make sure you're in the virtual environment and dependencies are installed:
```bash
pip install -r requirements.txt
```

### Issue: "Port 8000 already in use"

**Solution**: Change the port in `.env` or kill the process using port 8000:

**Windows:**
```bash
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

**Linux/Mac:**
```bash
lsof -i :8000
kill -9 <PID>
```

### Issue: "HUGGINGFACE_API_TOKEN not set"

**Solution**: Check that `.env` file exists and contains the token:
```bash
cat .env  # Linux/Mac
type .env  # Windows
```

### Issue: "Failed to fetch from Hugging Face"

**Possible causes**:
1. Invalid token
2. Network issues
3. Model loading (wait 10-20 seconds)
4. Rate limiting (wait and retry)

**Solution**: Check logs for specific error messages.

---

## 📊 Monitoring

### View Logs

The backend logs all operations:
```
INFO:     Started server process
INFO:     Received file: test.mp3, type: audio
INFO:     Transcribing audio (1234567 bytes) in en
INFO:     Transcription successful: 150 characters
INFO:     Translating text (150 chars): eng_Latn -> tam_Taml
INFO:     Translation successful: 180 characters
INFO:     Job abc-123 completed successfully
```

### Check Upload Directory

Generated files are stored in `uploads/`:
```
uploads/
└── {job_id}/
    ├── {job_id}_transcript.txt
    ├── {job_id}_translation.txt
    └── {job_id}_subtitles.srt
```

---

## 🚀 Deployment Options

### Option 1: Local Development
```bash
python main.py
```

### Option 2: Production with Gunicorn
```bash
pip install gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Option 3: Docker
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### Option 4: Cloud Platforms
- **Heroku**: Deploy with Procfile
- **AWS**: Use Elastic Beanstalk or Lambda
- **Google Cloud**: Use Cloud Run
- **Azure**: Use App Service

---

## ✅ Success Checklist

- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] `.env` file configured with HF token
- [ ] Backend server running (`python main.py`)
- [ ] Health check returns "healthy" (`http://localhost:8000/health`)
- [ ] API documentation accessible (`http://localhost:8000/docs`)
- [ ] Can process test file successfully

---

## 🎉 Next Steps

Once the backend is running:

1. **Start Flutter App**: Run `flutter run -d windows` or `flutter run -d chrome`
2. **Test Media Translation**: Upload a file in the app
3. **Verify**: Check that transcription and translation work
4. **Monitor**: Watch backend logs for processing status

---

## 📞 Support

If you encounter issues:

1. Check backend logs for error messages
2. Verify `.env` configuration
3. Test with curl or Postman first
4. Check Hugging Face API status
5. Ensure network connectivity

---

**🎊 Your backend is now ready to handle media translation requests!**
