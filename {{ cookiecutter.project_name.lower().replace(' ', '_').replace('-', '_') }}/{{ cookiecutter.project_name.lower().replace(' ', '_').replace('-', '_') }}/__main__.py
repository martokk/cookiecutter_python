from loguru import logger
from {{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}.core import app

# Configure Loguru Logger
logger.add(LOG_FILE, level="TRACE", rotation="50 MB")


if __name__ == "__main__":
    app()
