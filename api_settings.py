"""Settings for the API."""

from pydantic import AnyHttpUrl, BaseSettings, Field


class Settings(BaseSettings):
    """Settings for the API."""

    # CORS config
    CORS_ORIGINS: list[str | AnyHttpUrl] = Field(
        default=["*"],
        env="CORS_ORIGINS",
        description="A list of origins to allow CORS requests from.",
    )
    # Azure CV config
    AZ_CV_KEY: str = Field(
        default=...,
        env="AZ_CV_KEY",
        description="The Azure Computer Vision instance key.",
    )
    AZ_CV_ENDPOINT: str = Field(
        default=...,
        env="AZ_CV_ENDPOINT",
        description="The Azure Computer Vision instance endpoint.",
    )
    # Hugging Face config
    HF_TOKEN: str = Field(
        default=...,
        env="HF_TOKEN",
        description="The Hugging Face token for authenticating with the inference API.",
    )
    # Azure AD config
    AZ_AD_TENANT_DOMAIN: str = Field(
        default=...,
        env="AZ_AD_TENANT_DOMAIN",
        description="The Azure AD directory domain.",
    )
    AZ_TENANT_ID: str = Field(
        default=...,
        env="AZ_TENANT_ID",
        description="The Azure AD tenant ID.",
    )
    AZ_AD_APP_CLIENT_ID: str = Field(
        default=...,
        env="AZ_AD_APP_CLIENT_ID",
        description="The Azure AD app client ID.",
    )
    AZ_AD_DOCS_CLIENT_ID: str = Field(
        default=...,
        env="AZ_AD_DOCS_CLIENT_ID",
        description="The Azure AD docs (Swagger) client ID.",
    )

    class Config:  # pylint: disable=too-few-public-methods
        """Config for the environment."""

        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


SETTINGS = Settings()
