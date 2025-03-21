import asyncio
from logging import getLogger

from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
from quest.core.config import settings

logger = getLogger(__name__)


default_app: FastAPI | None = None


def get_default_app() -> FastAPI:
    from quest.api.router import api_router

    global default_app
    if default_app:
        return default_app

    openapi_url = None
    app = FastAPI(title=settings.PROJECT_NAME, openapi_url=openapi_url)
    app.include_router(api_router)

    default_app = app
    return app
