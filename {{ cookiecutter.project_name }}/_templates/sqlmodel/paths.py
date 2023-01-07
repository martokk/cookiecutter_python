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
# VIDEO_INFO_CACHE_PATH = CACHE_PATH / "video_info"

# Files
ENV_FILE = DATA_PATH / ".env"
DATABASE_FILE = DATA_PATH / "database.sqlite3"
LOG_FILE = LOGS_PATH / "log.log"
