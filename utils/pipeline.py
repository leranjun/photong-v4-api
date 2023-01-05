"""
Pipeline for generating music from an image.
"""

from typing import Optional

from .components import caption_to_prompt, generate_music, get_image_caption


def image_to_music(
    data: bytes,
    *,
    azure_key: str,
    azure_endpoint: str,
    hf_token: str,
    riffusion_seed: int,
    riffusion_seed_img: Optional[str] = None,
    timeout: Optional[float] = None,
) -> dict[str, str | float]:
    """
    Generate music from an image.

    Parameters:
        data (bytes): The image data.
        azure_key (str): The Azure API key.
        azure_endpoint (str): The Azure API endpoint.
        hf_token (str): The Hugging Face access token.
        riffusion_seed (int): The seed passed to Riffusion generation.
        riffusion_seed_img (Optional[str]): The seed image used as the initial image for Riffusion.
        timeout (Optional[float]): The timeout for API calls.

    Returns:
        dict[str, str | float]: The caption, prompt, audio, and duration. See `InferenceResponse`.

    Raises:
        HTTPException: If the API calls fail.
    """
    caption = get_image_caption(data, azure_key, azure_endpoint, timeout=timeout)
    prompt = caption_to_prompt(caption, hf_token, timeout=timeout)
    audio, duration = generate_music(prompt, riffusion_seed, riffusion_seed_img)
    return {
        "caption": caption,
        "prompt": prompt,
        "audio": audio,
        "duration": duration,
    }
