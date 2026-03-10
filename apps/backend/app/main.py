from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import get_settings
from app.core.logging import configure_logging, get_logger

configure_logging()
logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(_: FastAPI):
    settings = get_settings()
    logger.info(
        "application_startup",
        extra={"environment": settings.environment, "app_name": settings.app_name},
    )
    yield
    logger.info("application_shutdown")


app = FastAPI(
    title="TrenBot Enterprise Backend",
    version="0.1.0",
    lifespan=lifespan,
)
app.include_router(api_router)

