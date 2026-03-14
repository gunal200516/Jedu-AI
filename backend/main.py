"""
JeduAI Media Translation Backend
FastAPI server for handling Hugging Face API calls
"""
import os
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pathlib import Path

from models.schemas import HealthResponse
from services.hf_client import HuggingFaceClient
from services.media_processor import MediaProcessor
from routes import media_translation

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="JeduAI Media Translation API",
    description="Backend proxy for Hugging Face media translation",
    version="1.0.0"
)

# Configure CORS
cors_origins = os.getenv("CORS_ORIGINS", "http://localhost:*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, use specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
HF_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "./uploads")

if not HF_TOKEN:
    logger.error("HUGGINGFACE_API_TOKEN not set in environment")
    raise ValueError("HUGGINGFACE_API_TOKEN is required")

# Create upload directory
Path(UPLOAD_DIR).mkdir(parents=True, exist_ok=True)

# Initialize HF client and media processor
hf_client = HuggingFaceClient(api_token=HF_TOKEN)
media_processor = MediaProcessor(hf_client=hf_client, upload_dir=UPLOAD_DIR)

# Set processor in routes
media_translation.set_media_processor(media_processor)

# Include routers
app.include_router(media_translation.router)


@app.get("/", response_model=HealthResponse)
async def root():
    """Root endpoint - health check"""
    return HealthResponse(
        status="healthy",
        message="JeduAI Media Translation Backend is running",
        hf_token_configured=bool(HF_TOKEN)
    )


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        message="Service is operational",
        hf_token_configured=bool(HF_TOKEN)
    )


if __name__ == "__main__":
    import uvicorn
    
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    
    logger.info(f"Starting server on {host}:{port}")
    logger.info(f"Upload directory: {UPLOAD_DIR}")
    logger.info(f"HF Token configured: {bool(HF_TOKEN)}")
    
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=True,
        log_level="info"
    )
