"""Collection of services."""
from tempfile import SpooledTemporaryFile
from typing import IO, Dict, Optional, Union

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
