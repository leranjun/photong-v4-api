"""Schemas for the API."""
# pylint: disable=too-few-public-methods

from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Response schema for health check."""

    message: str


class InferenceResponse(BaseModel):
    """Response schema for inference."""

    caption: str
    prompt: str
    audio: str
    duration: float


class InferencePromptResponse(BaseModel):
    """Response schema for inference with prompt."""

    audio: str
    duration: float
