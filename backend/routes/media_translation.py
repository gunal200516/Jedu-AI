"""
Media Translation API Routes
"""
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
import logging
from models.schemas import MediaProcessResponse, MediaType
from services.media_processor import MediaProcessor

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/media", tags=["media"])

# Global processor instance (will be set by main.py)
media_processor: MediaProcessor = None


def set_media_processor(processor: MediaProcessor):
    """Set the global media processor instance"""
    global media_processor
    media_processor = processor


@router.post("/process", response_model=MediaProcessResponse)
async def process_media(
    file: UploadFile = File(...),
    sourceLanguage: str = Form(...),
    targetLanguage: str = Form(...),
    mediaType: str = Form(...)
):
    """
    Process uploaded media file for transcription and translation
    
    Args:
        file: Uploaded audio/video file
        sourceLanguage: Source language name
        targetLanguage: Target language name
        mediaType: Type of media ('audio' or 'video')
        
    Returns:
        Processing results with transcript, translation, and download links
    """
    try:
        logger.info(f"Received file: {file.filename}, type: {mediaType}")
        
        # Read file bytes
        file_bytes = await file.read()
        
        # Validate file size
        file_size_mb = len(file_bytes) / (1024 * 1024)
        if mediaType == "audio" and file_size_mb > 25:
            raise HTTPException(status_code=413, detail="Audio file too large (max 25MB)")
        if mediaType == "video" and file_size_mb > 100:
            raise HTTPException(status_code=413, detail="Video file too large (max 100MB)")
        
        # Process the media
        result = await media_processor.process_media(
            file_bytes=file_bytes,
            filename=file.filename,
            source_language=sourceLanguage,
            target_language=targetLanguage,
            media_type=mediaType
        )
        
        return MediaProcessResponse(**result)
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Processing error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/download/{job_id}/{filename}")
async def download_file(job_id: str, filename: str):
    """
    Download generated file
    
    Args:
        job_id: Job ID
        filename: File name (transcript.txt, translation.txt, or subtitles.srt)
        
    Returns:
        File download response
    """
    try:
        # Construct file path
        upload_dir = Path(media_processor.upload_dir)
        job_dir = upload_dir / job_id
        
        # Map filename to actual file
        file_map = {
            "transcript.txt": f"{job_id}_transcript.txt",
            "translation.txt": f"{job_id}_translation.txt",
            "subtitles.srt": f"{job_id}_subtitles.srt",
        }
        
        actual_filename = file_map.get(filename)
        if not actual_filename:
            raise HTTPException(status_code=404, detail="File not found")
        
        file_path = job_dir / actual_filename
        
        if not file_path.exists():
            raise HTTPException(status_code=404, detail="File not found")
        
        return FileResponse(
            path=file_path,
            filename=filename,
            media_type="text/plain" if filename.endswith(".txt") else "application/x-subrip"
        )
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Download error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
