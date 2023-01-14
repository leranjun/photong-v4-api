"""Main application file for the API."""
import os
from typing import Optional

import dotenv
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from utils import components, pipeline
from utils.schemas import HealthResponse, InferencePromptResponse, InferenceResponse

dotenv.load_dotenv()

AZ_KEY = os.getenv("AZ_CV_KEY", "")
if not AZ_KEY:
    raise ValueError("AZ_CV_KEY environment variable not set.")
AZ_ENDPOINT = os.getenv("AZ_CV_ENDPOINT", "")
if not AZ_ENDPOINT:
    raise ValueError("AZ_CV_ENDPOINT environment variable not set.")
HF_TOKEN = os.getenv("HF_TOKEN", "")
if not HF_TOKEN:
    raise ValueError("HF_TOKEN environment variable not set.")
CORS_ORIGIN_STR = os.getenv("CORS_ORIGINS", "")
if not CORS_ORIGIN_STR:
    raise ValueError("CORS_ORIGINS environment variable not set.")
CORS_ORIGINS = CORS_ORIGIN_STR.split(",")

app = FastAPI(
    title="Photong v3 API",
    description="The backend generator for Photong v3.",
    version="3.0.0",
    openapi_tags=[
        {"name": "Root", "description": "Root endpoint for the API."},
        {
            "name": "Inference",
            "description": "Endpoints for generating music and image captions.",
        },
    ],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True if CORS_ORIGINS[0] != "*" else False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Root"], response_model=HealthResponse)
async def root() -> dict[str, str]:
    """Root endpoint for the API."""
    return {"message": "Server is running."}


@app.post("/infer", tags=["Inference"], response_model=InferenceResponse)
async def infer(
    file: UploadFile, seed: int, alpha: float = 0.25, seed_img: Optional[str] = None
) -> dict[str, str | float]:
    """Generate music from an image."""
    img = await file.read()
    return pipeline.image_to_music(
        img,
        azure_key=AZ_KEY,
        azure_endpoint=AZ_ENDPOINT,
        hf_token=HF_TOKEN,
        riffusion_seed=seed,
        riffusion_alpha=alpha,
        riffusion_seed_img=seed_img,
    )


@app.post(
    "/infer/with-prompt", tags=["Inference"], response_model=InferencePromptResponse
)
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
