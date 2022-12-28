import os

from dotenv import load_dotenv

from {{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}.paths import ENV_FILE

# --- Load Environment
load_dotenv(dotenv_path=ENV_FILE)

# --- Bind Environment variables

# Server
SERVER_IP = str(os.environ.get("SERVER_IP", "0.0.0.0"))
SERVER_PORT = int(os.environ.get("SERVER_PORT", 5000))

# Database
DATABASE_ECHO = os.environ.get("DATABASE_ECHO", "True") == "True"

# Cache
USE_CACHE = bool(os.environ.get("USE_CACHE", True))