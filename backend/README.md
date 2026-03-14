# JeduAI Media Translation Backend

FastAPI backend server for handling Hugging Face API calls and solving CORS issues.

## 🚀 Quick Start

### Windows

Double-click `start_backend.bat` or run:
```bash
start_backend.bat
```

### Manual Start

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Start server
python main.py
```

## ✅ Verify Backend is Running

Open browser: `http://localhost:8000`

You should see:
```json
{
  "status": "healthy",
  "message": "JeduAI Media Translation Backend is running",
  "hf_token_configured": true
}
```

## 📡 API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `POST /api/media/process` - Process media file
- `GET /api/media/download/{job_id}/{filename}` - Download file
- `GET /docs` - Interactive API documentation

## 📚 Documentation

See `BACKEND_SETUP_GUIDE.md` for complete setup instructions.

## 🔧 Configuration

Edit `.env` file to configure:
- Hugging Face API token
- Server host and port
- CORS origins
- File size limits

## 🆘 Troubleshooting

### Port 8000 already in use

Change port in `.env`:
```env
PORT=8001
```

### Module not found

Install dependencies:
```bash
pip install -r requirements.txt
```

### HF token not configured

Check `.env` file contains:
```env
HUGGINGFACE_API_TOKEN=your_token_here
```

## 📞 Support

For issues, check:
1. Backend logs in terminal
2. `.env` configuration
3. Python version (3.8+)
4. Network connectivity
