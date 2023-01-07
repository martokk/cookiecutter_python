import uvicorn
from loguru import logger

from {{ cookiecutter.project_module }}.config import SERVER_IP, SERVER_PORT


def start_server() -> None:
    uvicorn.run(
        "{{ cookiecutter.project_module }}.core.app:app",
        host=SERVER_IP,
        port=SERVER_PORT,
        log_level="debug",
        reload=True,
        app_dir="",
    )
    logger.success("Uvicorn Server started")
