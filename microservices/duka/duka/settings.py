"""Settings for Duka Core Project."""
from typing import List

from pydantic import BaseSettings


class EnvSettings(BaseSettings):
    """Base settings for Duka Core."""

    PROJECT_NAME: str = "Duka Core"

    PROJECT_DESCRIPTION: str = "A microservice that has the main logic for Duka project"

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
