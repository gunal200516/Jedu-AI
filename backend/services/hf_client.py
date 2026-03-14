"""
Hugging Face API Client
Handles all communication with Hugging Face Inference API
"""
import httpx
import asyncio
from typing import Optional
import logging

logger = logging.getLogger(__name__)


class HuggingFaceClient:
    """Client for Hugging Face Inference API"""
    
    WHISPER_MODEL = "openai/whisper-large-v3"
    NLLB_MODEL = "facebook/nllb-200-distilled-600M"
    BASE_URL = "https://api-inference.huggingface.co/models"
    
    def __init__(self, api_token: str):
        """
        Initialize HF client
        
        Args:
            api_token: Hugging Face API token
        """
        self.api_token = api_token
        self.timeout = 120.0
        self.max_retries = 3
        self.retry_delay = 2
    
    async def transcribe_audio(
        self,
        audio_bytes: bytes,
        source_language: str
    ) -> str:
        """
        Transcribe audio using Whisper model
        
        Args:
            audio_bytes: Raw audio file bytes
            source_language: Source language code (ISO 639-1)
            
        Returns:
            Transcribed text
            
        Raises:
            Exception: If transcription fails
        """
        url = f"{self.BASE_URL}/{self.WHISPER_MODEL}"
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/octet-stream",
        }
        
        logger.info(f"Transcribing audio ({len(audio_bytes)} bytes) in {source_language}")
        
        for attempt in range(self.max_retries):
            try:
                async with httpx.AsyncClient(timeout=self.timeout) as client:
                    response = await client.post(url, headers=headers, content=audio_bytes)
                    
                    if response.status_code == 200:
                        result = response.json()
                        transcript = result.get("text", "")
                        logger.info(f"Transcription successful: {len(transcript)} characters")
                        return transcript.strip()
                    
                    elif response.status_code == 503:
                        # Model loading
                        logger.warning(f"Model loading, retrying in {self.retry_delay}s...")
                        await asyncio.sleep(self.retry_delay)
                        continue
                    
                    elif response.status_code == 429:
                        # Rate limited
                        delay = self.retry_delay * (attempt + 1)
                        logger.warning(f"Rate limited, retrying in {delay}s...")
                        await asyncio.sleep(delay)
                        continue
                    
                    else:
                        error_msg = f"Transcription failed: {response.status_code} - {response.text}"
                        logger.error(error_msg)
                        raise Exception(error_msg)
            
            except httpx.TimeoutException:
                logger.warning(f"Request timeout, attempt {attempt + 1}/{self.max_retries}")
                if attempt < self.max_retries - 1:
                    await asyncio.sleep(self.retry_delay)
                else:
                    raise Exception("Transcription timeout")
            
            except Exception as e:
                logger.error(f"Transcription error: {str(e)}")
                if attempt < self.max_retries - 1:
                    await asyncio.sleep(self.retry_delay)
                else:
                    raise
        
        raise Exception("Transcription failed after all retries")
    
    async def translate_text(
        self,
        text: str,
        source_language: str,
        target_language: str
    ) -> str:
        """
        Translate text using NLLB model
        
        Args:
            text: Text to translate
            source_language: Source language code (NLLB format)
            target_language: Target language code (NLLB format)
            
        Returns:
            Translated text
            
        Raises:
            Exception: If translation fails
        """
        url = f"{self.BASE_URL}/{self.NLLB_MODEL}"
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json",
        }
        payload = {
            "inputs": text,
            "parameters": {
                "src_lang": source_language,
                "tgt_lang": target_language,
            }
        }
        
        logger.info(f"Translating text ({len(text)} chars): {source_language} -> {target_language}")
        
        for attempt in range(self.max_retries):
            try:
                async with httpx.AsyncClient(timeout=self.timeout) as client:
                    response = await client.post(url, headers=headers, json=payload)
                    
                    if response.status_code == 200:
                        result = response.json()
                        
                        # Handle different response formats
                        if isinstance(result, list) and len(result) > 0:
                            translation = result[0].get("translation_text", "")
                        elif isinstance(result, dict):
                            translation = result.get("translation_text", "")
                        else:
                            raise Exception("Unexpected response format")
                        
                        logger.info(f"Translation successful: {len(translation)} characters")
                        return translation.strip()
                    
                    elif response.status_code == 503:
                        # Model loading
                        logger.warning(f"Model loading, retrying in {self.retry_delay}s...")
                        await asyncio.sleep(self.retry_delay)
                        continue
                    
                    elif response.status_code == 429:
                        # Rate limited
                        delay = self.retry_delay * (attempt + 1)
                        logger.warning(f"Rate limited, retrying in {delay}s...")
                        await asyncio.sleep(delay)
                        continue
                    
                    else:
                        error_msg = f"Translation failed: {response.status_code} - {response.text}"
                        logger.error(error_msg)
                        raise Exception(error_msg)
            
            except httpx.TimeoutException:
                logger.warning(f"Request timeout, attempt {attempt + 1}/{self.max_retries}")
                if attempt < self.max_retries - 1:
                    await asyncio.sleep(self.retry_delay)
                else:
                    raise Exception("Translation timeout")
            
            except Exception as e:
                logger.error(f"Translation error: {str(e)}")
                if attempt < self.max_retries - 1:
                    await asyncio.sleep(self.retry_delay)
                else:
                    raise
        
        raise Exception("Translation failed after all retries")
