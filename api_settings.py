"""Settings for the API."""

from pydantic import AnyHttpUrl, BaseSettings, Field

# from fastapi_azure_auth import (
#     B2CMultiTenantAuthorizationCodeBearer,
#     MultiTenantAzureAuthorizationCodeBearer,
# )


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

# __APP_BASE_DOMAIN = (
#     f"https://{SETTINGS.AZ_AD_TENANT_DOMAIN}/{SETTINGS.AZ_AD_APP_CLIENT_ID}"
# )
# __OAUTH_BASE_DOMAIN = f"https://login.microsoftonline.com/{SETTINGS.AZ_TENANT_ID}"

# AZ_SCHEME = MultiTenantAzureAuthorizationCodeBearer(
# AZ_SCHEME = B2CMultiTenantAuthorizationCodeBearer(
#     app_client_id=SETTINGS.AZ_AD_APP_CLIENT_ID,
#     openid_config_use_app_id=True,
#     scopes={
#         f"{__APP_BASE_DOMAIN}/user_impersonation": "user_impersonation",
#     },
#     validate_iss=False,
# )
# AZ_SCHEME_DOCS = B2CMultiTenantAuthorizationCodeBearer(
#     app_client_id=SETTINGS.AZ_AD_APP_CLIENT_ID,
#     openapi_authorization_url=f"{__OAUTH_BASE_DOMAIN}/oauth2/v2.0/authorize",
#     openapi_token_url=f"{__OAUTH_BASE_DOMAIN}/oauth2/v2.0/token",
#     openid_config_url=f"{__OAUTH_BASE_DOMAIN}/v2.0/.well-known/openid-configuration",
#     scopes={
#         f"{__APP_BASE_DOMAIN}/user_impersonation": "user_impersonation",
#     },
#     validate_iss=False,
# )
