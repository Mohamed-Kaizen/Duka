"""App for Duka File Uploader Project."""
import logging
import sys
from typing import Any, Dict, Union

from fastapi import Depends, FastAPI, File, HTTPException, Request, UploadFile, status
from fastapi.responses import ORJSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from loguru import logger
from starlette.middleware.cors import CORSMiddleware

from .logger import InterceptHandler, log_format
from .schema import CHANGE_USER_PICTURE
from .services import graphql, upload
from .settings import REDIS, SETTINGS, EnvSettings

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


@AuthJWT.load_config
def get_config() -> EnvSettings:
    """A callback to get your configuration."""
    return SETTINGS


@app.exception_handler(AuthJWTException)
def auth_exception_handler(request: Request, exc: AuthJWTException) -> ORJSONResponse:
    """Exception handler for authjwt."""
    return ORJSONResponse(status_code=exc.status_code, content={"detail": exc.message})


@AuthJWT.token_in_denylist_loader
def check_if_token_in_deny_list(
    decrypted_token: Dict[str, Any]
) -> Union[str, None, bool]:
    """Checking if the tokens jti is in the deny list set."""
    jti = decrypted_token["jti"]
    entry = REDIS.get(jti)
    return entry and entry == "true"


@app.post("/user/", response_class=ORJSONResponse)
async def upload_user_picture(
    file: UploadFile = File(...), authorize: AuthJWT = Depends()
) -> Dict[str, str]:
    """Upload new profile picture."""
    authorize.jwt_required()

    user_id = authorize.get_jwt_subject()

    url = upload(
        bucket="users",
        file=file.file,
        file_content_type=file.content_type,
        file_path=f"{user_id}/{file.filename}",
    )

    r = await graphql(
        query=CHANGE_USER_PICTURE
        % {
            "user_id": user_id,
            "picture": url,
        }
    )

    if "errors" in r.json():

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User not found.",
        )

    return {"detail": url}


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
