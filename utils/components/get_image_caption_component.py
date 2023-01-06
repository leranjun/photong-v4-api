"""Generate image caption."""
from typing import Optional
from urllib.parse import urljoin

import requests


def get_image_caption(
    data: bytes, key: str, endpoint: str, *, timeout: Optional[float] = 30
) -> str:
    """
    Generate image caption using Azure Computer Vision API.

    Parameters:
        data (bytes): The image data.
        key (str): The Azure API key.
        endpoint (str): The Azure API endpoint.
        timeout (Optional[float]): The timeout for the API call.

    Returns:
        str: The image caption.

    Raises:
        HTTPException: If the API call fails.
    """
    url = urljoin(endpoint, "computervision/imageanalysis:analyze")

    headers = {
        "Ocp-Apim-Subscription-Key": key,
        "Content-Type": "application/octet-stream",
    }

    params = {
        "features": "Description",
        "model-version": "latest",
        "language": "en",
        "api-version": "2022-10-12-preview",
    }

    response = requests.post(
        url,
        headers=headers,
        params=params,
        data=data,
        timeout=timeout,
    )
    response.raise_for_status()
    res = response.json()

    caption: str = res["descriptionResult"]["values"][0]["text"]
    return caption
