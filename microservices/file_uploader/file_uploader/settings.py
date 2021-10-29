"""Settings for Duka File Uploader Project."""
from typing import List, Set

import boto3
import botocore
from botocore.client import Config
from pydantic import BaseSettings
from redis import Redis


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

    MINIO_ROOT_USER: str

    MINIO_ROOT_PASSWORD: str

    MINIO_ENDPOINT_URL: str

    MINIO_CONTAINER_URL: str

    HASURA_ENDPOINT_URL: str

    authjwt_secret_key: str

    authjwt_denylist_enabled: bool = True

    authjwt_denylist_token_checks: Set[str] = {"access", "refresh"}


SETTINGS = EnvSettings()


REDIS = Redis(host="redis_auth", port=6379, db=0, decode_responses=True)

S3 = boto3.client(
    "s3",
    endpoint_url=SETTINGS.MINIO_CONTAINER_URL,
    aws_access_key_id=SETTINGS.MINIO_ROOT_USER,
    aws_secret_access_key=SETTINGS.MINIO_ROOT_PASSWORD,
    config=Config(signature_version=botocore.UNSIGNED),
)
