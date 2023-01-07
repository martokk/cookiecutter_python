from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles
from fastapi_utils.tasks import repeat_every
from loguru import logger

from {{ cookiecutter.project_module }}.api.v1.api import api_router
from {{ cookiecutter.project_module }}.db.database import create_db_and_tables

# Initialize FastAPI App
app = FastAPI()
app.include_router(api_router)
# app.mount("/static", StaticFiles(directory=STATIC_FILES_PATH), name="static")

@app.on_event("startup")  # type: ignore
async def on_startup() -> None:
    """
    On Statup:
        - create database and tables.
    """
    return await create_db_and_tables()


# @app.on_event("startup")  # type: ignore
# @repeat_every(seconds=60, wait_first=True)
# async def repeating_task() -> None:
#     """
#     Repeat Every n seconds:
#         - ...
#     """
#     logger.info("doing something")
#     pass
#     logger.success("Completed.")


@app.get("/")
async def root() -> dict[str, str]:
    """
    Server root, return simple api status.
    """
    return {"api_status": "OK"}
