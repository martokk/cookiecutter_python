from loguru import logger
from {{ cookiecutter.__project_module }}.core import app

# Configure Loguru Logger
logger.add(LOG_FILE, level="TRACE", rotation="50 MB")


if __name__ == "__main__":
    app()
