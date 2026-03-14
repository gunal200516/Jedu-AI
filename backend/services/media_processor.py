"""
Media Processing Service
Orchestrates the complete media translation workflow
"""
import os
import uuid
import logging
from pathlib import Path
from typing import Dict, Any, Optional
from services.hf_client import HuggingFaceClient
from utils.language_codes import get_whisper_code, get_nllb_code
from utils.subtitle_generator import generate_srt_content

logger = logging.getLogger(__name__)


class MediaProcessor:
    """Handles media file processing and translation"""
    
    def __init__(self, hf_client: HuggingFaceClient, upload_dir: str):
        """
        Initialize media processor
        
        Args:
            hf_client: Hugging Face API client
            upload_dir: Directory for storing uploaded files
        """
        self.hf_client = hf_client
        self.upload_dir = Path(upload_dir)
        self.upload_dir.mkdir(parents=True, exist_ok=True)
    
    async def process_media(
        self,
        file_bytes: bytes,
        filename: str,
        source_language: str,
        target_language: str,
        media_type: str
    ) -> Dict[str, Any]:
        """
        Process media file: transcribe and translate
        
        Args:
            file_bytes: Raw file bytes
            filename: Original filename
            source_language: Source language name
            target_language: Target language name
            media_type: 'audio' or 'video'
            
        Returns:
            Dictionary with processing results
        """
        job_id = str(uuid.uuid4())
        logger.info(f"Processing job {job_id}: {filename}")
        
        try:
            # Step 1: Transcribe audio
            whisper_code = get_whisper_code(source_language)
            transcript = await self.hf_client.transcribe_audio(
                file_bytes,
                whisper_code
            )
            
            if not transcript:
                raise Exception("Transcription returned empty result")
            
            # Step 2: Translate transcript
            src_nllb = get_nllb_code(source_language)
            tgt_nllb = get_nllb_code(target_language)
            translation = await self.hf_client.translate_text(
                transcript,
                src_nllb,
                tgt_nllb
            )
            
            if not translation:
                raise Exception("Translation returned empty result")
            
            # Step 3: Generate subtitle content (for video)
            subtitle_content = None
            if media_type == "video":
                subtitle_content = generate_srt_content(transcript, translation)
            
            # Step 4: Save files
            job_dir = self.upload_dir / job_id
            job_dir.mkdir(parents=True, exist_ok=True)
            
            # Save transcript
            transcript_path = job_dir / f"{job_id}_transcript.txt"
            transcript_path.write_text(transcript, encoding='utf-8')
            
            # Save translation
            translation_path = job_dir / f"{job_id}_translation.txt"
            translation_path.write_text(translation, encoding='utf-8')
            
            # Save subtitle (if video)
            subtitle_path = None
            if subtitle_content:
                subtitle_path = job_dir / f"{job_id}_subtitles.srt"
                subtitle_path.write_text(subtitle_content, encoding='utf-8')
            
            logger.info(f"Job {job_id} completed successfully")
            
            return {
                "success": True,
                "jobId": job_id,
                "transcript": transcript,
                "translation": translation,
                "subtitleContent": subtitle_content,
                "downloads": {
                    "transcriptTxt": f"/api/media/download/{job_id}/transcript.txt",
                    "translationTxt": f"/api/media/download/{job_id}/translation.txt",
                    "subtitleSrt": f"/api/media/download/{job_id}/subtitles.srt" if subtitle_content else None,
                    "translatedAudio": None,
                    "processedVideo": None,
                },
                "status": "completed"
            }
        
        except Exception as e:
            logger.error(f"Job {job_id} failed: {str(e)}")
            return {
                "success": False,
                "jobId": job_id,
                "error": str(e),
                "status": "failed"
            }
