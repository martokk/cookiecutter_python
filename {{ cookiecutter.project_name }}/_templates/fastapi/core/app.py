from fastapi import FastAPI

# from fastapi_utils.tasks import repeat_every
from {{ cookiecutter.project_module }}.core.logger import logger
from {{ cookiecutter.project_module }}.core.notify import notify

from {{ cookiecutter.project_module }}.api.v1.api import api_router
from {{ cookiecutter.project_module }}.db.database import create_db_and_tables
from {{ cookiecutter.project_module }}.paths import LOG_FILE
from {{ cookiecutter.project_module }}.constants import PACKAGE_NAME
from {{ cookiecutter.project_module }}.config import ENV_NAME

# Configure Loguru Logger
# Initialize FastAPI App

app = FastAPI()
app.debug = True
app.include_router(api_router)
# app.mount("/feed", StaticFiles(directory=FEEDS_PATH), name="feed")


@app.on_event("startup")  # type: ignore
async def on_startup() -> None:
    """
    On Startup:
        - create database and tables.
    """
    logger.info("--- Start FastAPI ---")
    logger.debug("Starting FastAPI App...")
    await create_db_and_tables()
    await notify(text=f"{PACKAGE_NAME}('{ENV_NAME}') started.")


# @app.on_event("startup")  # type: ignore
# @repeat_every(seconds=REFRESH_VIDEOS_INTERVAL_MINUTES * 60, wait_first=True)
# async def repeating_refresh_videos() -> None:
#     """
#     Fetches new data for all Videos that meet criteria.
#     """
#     logger.debug("Refreshing Videos...")
#     refreshed_videos = await refresh_all_videos(older_than_hours=8)
#     logger.success(f"Completed refreshing {len(refreshed_videos)} Videos.")


@app.get("/")
async def root() -> dict[str, str]:
    """
    Server root, return simple api status.
    """
    return {"api_status": "OK"}
