"""Settings for Duka File Uploader Project."""
from typing import List, Set

from pydantic import BaseSettings


class EnvSettings(BaseSettings):
    """Base settings for Duka File Uploader."""

    PROJECT_NAME: str = "Duka File Uploader"

    PROJECT_DESCRIPTION: str = "A microservice that handle all file uploading for Duka project"

    DOCS_URL: str = "/docs"

    REDOC_URL: str = "/redoc"

    OPENAPI_URL: str = "/openapi.json"

    ALLOWED_HOSTS: List[str] = ["*"]

    CORS_ORIGINS: List[str] = ["*"]

    CORS_ALLOW_CREDENTIALS: bool = True

    CORS_ALLOW_METHODS: List[str] = ["*"]

    CORS_ALLOW_HEADERS: List[str] = ["*"]

    LOG_LEVEL: str = "DEBUG"

    HASURA_GRAPHQL_ADMIN_SECRET: str

    HASURA_ENDPOINT_URL: str


SETTINGS = EnvSettings()
