"""
Subtitle generation utilities
"""
from typing import List, Tuple


def generate_srt_content(
    transcript: str,
    translation: str,
    words_per_subtitle: int = 10,
    seconds_per_word: float = 0.4
) -> str:
    """
    Generate SRT subtitle content from transcript and translation
    
    Args:
        transcript: Original transcript text
        translation: Translated text
        words_per_subtitle: Number of words per subtitle chunk
        seconds_per_word: Duration per word in seconds
        
    Returns:
        SRT formatted subtitle content
    """
    translated_words = translation.split()
    subtitles = []
    
    index = 1
    current_time = 0.0
    
    for i in range(0, len(translated_words), words_per_subtitle):
        end_index = min(i + words_per_subtitle, len(translated_words))
        chunk = ' '.join(translated_words[i:end_index])
        duration = (end_index - i) * seconds_per_word
        
        start_time = format_srt_time(current_time)
        end_time = format_srt_time(current_time + duration)
        
        subtitles.append(f"{index}\n{start_time} --> {end_time}\n{chunk}\n")
        
        index += 1
        current_time += duration
    
    return '\n'.join(subtitles)


def format_srt_time(seconds: float) -> str:
    """
    Format time for SRT format (HH:MM:SS,mmm)
    
    Args:
        seconds: Time in seconds
        
    Returns:
        Formatted time string
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds % 1) * 1000)
    
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"
