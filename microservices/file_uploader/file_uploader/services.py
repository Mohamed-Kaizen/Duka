"""Collection of services."""
from tempfile import SpooledTemporaryFile
from typing import IO, Dict, Optional, Union

import httpx
from botocore.exceptions import ClientError

from .settings import S3, SETTINGS


async def graphql(*, query: str, variables: Optional[Dict] = None) -> httpx.Response:
    """Execute a graphql query."""
    async with httpx.AsyncClient() as client:
        r = await client.post(
            SETTINGS.HASURA_ENDPOINT_URL,
            json={
                "query": query,
                "variables": variables,
            },
            headers={"x-hasura-admin-secret": SETTINGS.HASURA_GRAPHQL_ADMIN_SECRET},
        )
        return r


def upload(
    *,
    bucket: str,
    file: Union[SpooledTemporaryFile, SpooledTemporaryFile[Union[str, bytes]], IO],
    file_content_type: str,
    file_path: str
) -> str:
    """Upload files to aws s3 or Minio storage."""
    S3.put_object(
        Bucket=bucket,
        Key=file_path,
        ACL="public-read",
        Body=file,
        ContentType=file_content_type,
    )

    return S3.generate_presigned_url(
        "get_object",
        Params={"Bucket": bucket, "Key": file_path},
        ExpiresIn=0,
    ).replace(SETTINGS.MINIO_CONTAINER_URL, SETTINGS.MINIO_ENDPOINT_URL)
