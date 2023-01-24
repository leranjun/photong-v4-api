"""Inference router."""
from typing import Optional

from fastapi import APIRouter, UploadFile

from api_settings import SETTINGS
from utils import components, pipeline
from utils.schemas import InferencePromptResponse, InferenceResponse

router = APIRouter(
    prefix="/infer",
    tags=["Inference"],
)


@router.post("/", response_model=InferenceResponse)
async def infer(
    file: UploadFile, seed: int, alpha: float = 0.25, seed_img: Optional[str] = None
) -> dict[str, str | float]:
    """Generate music from an image."""
    img = await file.read()
    return pipeline.image_to_music(
        img,
        azure_key=SETTINGS.AZ_CV_KEY,
        azure_endpoint=SETTINGS.AZ_CV_ENDPOINT,
        hf_token=SETTINGS.HF_TOKEN,
        riffusion_seed=seed,
        riffusion_alpha=alpha,
        riffusion_seed_img=seed_img,
    )


@router.post("/with-prompt", response_model=InferencePromptResponse)
async def infer_with_prompt(
    prompt: str, seed: int, alpha: float = 0.25, seed_img: Optional[str] = None
) -> dict[str, str | float]:
    """Generate music from a prompt."""
    audio, duration = components.generate_music(
        prompt,
        seed=seed,
        alpha=alpha,
        seed_img=seed_img,
    )
    return {
        "audio": audio,
        "duration": duration,
    }
