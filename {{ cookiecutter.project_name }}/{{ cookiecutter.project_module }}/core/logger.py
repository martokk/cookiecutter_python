from loguru import logger as _logger

from {{ cookiecutter.project_module }}.config import LOG_LEVEL
from {{ cookiecutter.project_module }}.paths import LOG_FILE

_logger.add(LOG_FILE, level=LOG_LEVEL, rotation="10 MB")
_logger.info(f"Log level set by .env to '{LOG_LEVEL}'")

logger = _logger
