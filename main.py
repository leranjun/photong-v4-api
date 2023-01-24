"""Main application file for the API."""

# from fastapi import FastAPI, Security
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse

# from api_settings import AZ_SCHEME, SETTINGS
from api_settings import SETTINGS
from utils.schemas import HealthResponse

from inference_router import router

app = FastAPI(
    title="Photong v3 API",
    description="The backend generator for Photong v3.",
    version="3.0.0",
    openapi_tags=[
        {"name": "Root", "description": "Root endpoint for the API."},
        # {
        #     "name": "User",
        #     "description": "Endpoints for user information.",
        # },
        {
            "name": "Inference",
            "description": "Endpoints for generating music and image captions.",
        },
    ],
    # swagger_ui_oauth2_redirect_url="/oauth2-redirect",
    # swagger_ui_init_oauth={
    #     "usePkceWithAuthorizationCodeGrant": True,
    #     "clientId": SETTINGS.AZ_AD_DOCS_CLIENT_ID,
    # },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=SETTINGS.CORS_ORIGINS,
    allow_credentials=(SETTINGS.CORS_ORIGINS[0] != "*"),
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.on_event("startup")
# async def load_config() -> None:
#     """
#     Load OpenID config on startup.
#     """
#     await AZ_SCHEME.openid_config.load_config()


@app.get("/", tags=["Root"], response_model=HealthResponse)
async def root() -> dict[str, str]:
    """Root endpoint for the API."""
    return {"message": "Server is running."}


@app.get("/robots.txt", tags=["Root"], response_class=PlainTextResponse)
def robots() -> str:
    """Robots.txt endpoint."""
    return "User-agent: *\nDisallow: /"


# @app.get("/user", tags=["User"])
# async def user(user: dict = Security(AZ_SCHEME)) -> dict[str, str]:
#     """Get user information."""
#     return user


app.include_router(router)
