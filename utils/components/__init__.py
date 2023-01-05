"""
This module contains all the components of the pipeline.
"""
from .caption_to_prompt_component import caption_to_prompt
from .generate_music_component import generate_music
from .get_image_caption_component import get_image_caption

__all__ = [
    "caption_to_prompt",
    "generate_music",
    "get_image_caption",
]
