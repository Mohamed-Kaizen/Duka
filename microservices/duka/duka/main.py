"""App for Duka File Uploader Project."""
import logging
import sys

from fastapi import FastAPI, Response
from fastapi.responses import ORJSONResponse
from loguru import logger
from starlette.middleware.cors import CORSMiddleware

from .logger import InterceptHandler, log_format
from .models import HasuraEventTrigger
from .services import add_seats
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
