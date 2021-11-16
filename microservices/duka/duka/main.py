"""App for Duka File Uploader Project."""
import logging
import sys

from fastapi import FastAPI, Response
from fastapi.responses import ORJSONResponse
from loguru import logger
from starlette.middleware.cors import CORSMiddleware

from .logger import InterceptHandler, log_format
from .models import HasuraEventTrigger
from .services import add_seats, add_trip_bus_seat, add_trip_history, get_bus
from .settings import SETTINGS

app = FastAPI(
    title=SETTINGS.PROJECT_NAME,
    description=SETTINGS.PROJECT_DESCRIPTION,
    version="0.1.0",
    docs_url=SETTINGS.DOCS_URL,
    redoc_url=SETTINGS.REDOC_URL,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=SETTINGS.CORS_ORIGINS,
    allow_credentials=SETTINGS.CORS_ALLOW_CREDENTIALS,
    allow_methods=SETTINGS.CORS_ALLOW_METHODS,
    allow_headers=SETTINGS.CORS_ALLOW_HEADERS,
)


@app.post("/create-seat", response_class=ORJSONResponse)
async def create_seat(event_data: HasuraEventTrigger) -> Response:
    """Create seats for a bus."""
    created, message = await add_seats(
        bus_id=event_data.event.data.new.get("id"),
        seat_no=int(event_data.event.data.new.get("total_seat")) + 1,
    )

    if created:
        return Response(status_code=200, content=message)

    return Response(status_code=400, content=message)


@app.post("/create-trip-history", response_class=ORJSONResponse)
async def create_trip_history(event_data: HasuraEventTrigger) -> Response:
    """Create trip history."""
    bus_id = event_data.event.data.new.get("bus")

    _, data = await get_bus(bus_id=bus_id)

    created, message = await add_trip_history(
        bus_id=bus_id,
        driver_id=data.get("bus_by_pk").get("driver"),
        trip_id=event_data.event.data.new.get("trip"),
    )

    if created:
        return Response(status_code=200, content=message)

    return Response(status_code=400, content=message)


@app.post("/create-trip-bus-seat", response_class=ORJSONResponse)
async def create_trip_bus_seat(event_data: HasuraEventTrigger) -> Response:
    """Create seats for trip bus."""
    bus_id = event_data.event.data.new.get("bus")

    _, data = await get_bus(bus_id=bus_id)

    created, message = await add_trip_bus_seat(
        trip_bus_id=event_data.event.data.new.get("id"),
        seats=data.get("bus_by_pk").get("seats"),
    )

    if created:
        return Response(status_code=200, content=message)

    return Response(status_code=400, content=message)


logging.getLogger().handlers = [InterceptHandler()]
logger.configure(
    handlers=[
        {
            "sink": sys.stdout,
            "level": SETTINGS.LOG_LEVEL,
            "format": log_format,
        }
    ]
)
logger.add("logs/file_{time:YYYY-MM-DD}.log", level="TRACE", rotation="1 day")

logging.getLogger("uvicorn.access").handlers = [InterceptHandler()]
