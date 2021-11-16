"""Collection of services."""
from typing import Any, Optional

from python_graphql_client import GraphqlClient

from .models import PythonGraphqlClientResponse
from .schema import CREATE_SEATS, CREATE_TRIP_BUS_SEATS, CREATE_TRIP_HISTORY, GET_BUS
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


async def add_trip_history(
    *, bus_id: str, driver_id: str, trip_id: str
) -> tuple[bool, Any]:
    """Add trip history."""
    resp = await graphql(
        query=CREATE_TRIP_HISTORY,
        variables={"bus": bus_id, "driver": driver_id, "trip": trip_id},
    )

    if resp.error:
        return False, resp.error

    return True, "Trip History has been created."


async def get_bus(*, bus_id: str) -> tuple[bool, Any]:
    """Get bus info."""
    resp = await graphql(
        query=GET_BUS,
        variables={"id": bus_id},
    )

    if resp.error:
        return False, resp.error

    return True, resp.data


async def add_trip_bus_seat(*, trip_bus_id: str, seats: list[dict]) -> tuple[bool, Any]:
    """Add trip bus seats."""
    trip_bus_seats = [
        {
            "trip_bus": trip_bus_id,
            "status": "Available",
            "seat": f"{seat.get('id')}",
        }
        for seat in seats
    ]

    resp = await graphql(
        query=CREATE_TRIP_BUS_SEATS, variables={"objects": trip_bus_seats}
    )

    if resp.error:
        return False, resp.error

    return True, f"Seats has been added for trip_bus_id: {trip_bus_id}"
