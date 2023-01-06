"""
Generate a musical prompt from an image caption.
"""
from typing import Optional

import requests

PROMPT = """This tool can generate a musical prompt from an image prompt:
a place in China -> traditional Chinese music
a place in South America -> Latin American music
a man blowing a trumpet in a club -> jazz music with trumpets
a concert hall -> orchestral music with violins
a country house -> acoustic folk country guitar
a blooming flower -> passionate piano and strings
a sleeping baby -> serene lullaby, violin and piano
"""
API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"


def caption_to_prompt(
    caption: str, token: str, *, timeout: Optional[float] = 30
) -> str:
    """
    Generate a musical prompt using BLOOM.

    Parameters:
        caption (str): The image caption.
        token (str): The Hugging Face access token.
        timeout (Optional[float]): The timeout for the API call.

    Returns:
        str: The generated musical prompt.

    Raises:
        HTTPException: If the API calls fail.
    """
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"inputs": f"{PROMPT}{caption} -> "}
    response = requests.post(API_URL, headers=headers, json=payload, timeout=timeout)
    response.raise_for_status()
    res = response.json()

    gen: str = res[0]["generated_text"]
    gen = gen.replace(PROMPT, "").split("\n")[0].split("->")[1].strip()
    return gen
