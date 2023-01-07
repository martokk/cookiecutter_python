# PROJECT STRUCTURE
import os
from pathlib import Path

# Project Path
BASE_PATH = Path(os.path.dirname(os.path.abspath(__file__)))

# Folders
DATA_PATH = BASE_PATH / "data"

# Data Folder
LOGS_PATH = DATA_PATH / "logs"
CACHE_PATH = DATA_PATH / "cache"

# Cache Folders
# EXAMPLE_CACHE_PATH = CACHE_PATH / "example"

# Files
ENV_FILE = DATA_PATH / ".env"
LOG_FILE = LOGS_PATH / "log.log"
