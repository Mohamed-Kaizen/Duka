"""Collection of services."""
from typing import Any, Optional

from python_graphql_client import GraphqlClient

from .models import PythonGraphqlClientResponse
from .schema import CREATE_SEATS
from .settings import SETTINGS


async def graphql(
    *,
    query: str,
    variables: Optional[dict] = None,
    headers: Optional[dict] = None,
) -> PythonGraphqlClientResponse:
    """Execute a graphql query."""
    if headers is None:
        headers = {"x-hasura-admin-secret": SETTINGS.HASURA_GRAPHQL_ADMIN_SECRET}

    client = GraphqlClient(endpoint=SETTINGS.HASURA_ENDPOINT_URL, headers=headers)

    resp = await client.execute_async(query=query, variables=variables)

    return PythonGraphqlClientResponse(**resp)


async def add_seats(*, bus_id: str, seat_no: int) -> tuple[bool, Any]:
    """Add seats to an bus."""
    seats = [{"bus": bus_id, "name": f"{i}"} for i in range(1, seat_no)]

    resp = await graphql(query=CREATE_SEATS, variables={"objects": seats})

    if resp.error:
        return False, resp.error

    return True, f"{seat_no} has been added for bus_id: {bus_id}"
