"""
Pydantic models for request/response validation
"""
from pydantic import BaseModel, Field
from typing import Optional, Dict
from enum import Enum


class MediaType(str, Enum):
    """Media type enumeration"""
    AUDIO = "audio"
    VIDEO = "video"


class ProcessStatus(str, Enum):
    """Processing status enumeration"""
    PENDING = "pending"
    UPLOADING = "uploading"
    EXTRACTING = "extracting"
    TRANSCRIBING = "transcribing"
    TRANSLATING = "translating"
    GENERATING = "generating"
    COMPLETED = "completed"
    FAILED = "failed"


class MediaProcessRequest(BaseModel):
    """Request model for media processing"""
    sourceLanguage: str = Field(..., description="Source language code")
    targetLanguage: str = Field(..., description="Target language code")
    mediaType: MediaType = Field(..., description="Type of media (audio/video)")


class DownloadLinks(BaseModel):
    """Download links for generated files"""
    transcriptTxt: Optional[str] = None
    translationTxt: Optional[str] = None
    subtitleSrt: Optional[str] = None
    translatedAudio: Optional[str] = None
    processedVideo: Optional[str] = None


class MediaProcessResponse(BaseModel):
    """Response model for media processing"""
    success: bool
    jobId: str
    transcript: Optional[str] = None
    translation: Optional[str] = None
    subtitleContent: Optional[str] = None
    downloads: Optional[DownloadLinks] = None
    error: Optional[str] = None
    status: ProcessStatus = ProcessStatus.COMPLETED


class HealthResponse(BaseModel):
    """Health check response"""
    status: str
    message: str
    hf_token_configured: bool
