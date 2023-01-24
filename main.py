"""Main application file for the API."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse

from api_settings import SETTINGS
from inference_router import router
from utils.schemas import HealthResponse

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
    allow_origins=SETTINGS.CORS_ORIGINS,
    allow_credentials=(SETTINGS.CORS_ORIGINS[0] != "*"),
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Root"], response_model=HealthResponse)
async def root() -> dict[str, str]:
    """Root endpoint for the API."""
    return {"message": "Server is running."}


@app.get("/robots.txt", tags=["Root"], response_class=PlainTextResponse)
def robots() -> str:
    """Robots.txt endpoint."""
    return "User-agent: *\nDisallow: /"


app.include_router(router)
