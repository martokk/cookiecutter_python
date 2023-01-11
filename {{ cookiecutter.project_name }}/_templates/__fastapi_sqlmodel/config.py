import os

from dotenv import load_dotenv

from {{ cookiecutter.project_module }}.paths import ENV_FILE

# --- Load Environment
load_dotenv(dotenv_path=ENV_FILE)

# --- Bind Environment variables
ENV_NAME = str(os.environ.get("ENV_NAME", "Unspecified ENV_NAME"))

# Server
SERVER_IP = str(os.environ.get("SERVER_IP", "0.0.0.0"))
SERVER_PORT = int(os.environ.get("SERVER_PORT", 5000))
BASE_DOMAIN = str(os.environ.get("BASE_DOMAIN", f"{SERVER_IP}:{SERVER_PORT}"))
BASE_URL = str(os.environ.get("BASE_URL", f"http://{BASE_DOMAIN}"))
UVICORN_RELOAD = str(os.environ.get("UVICORN_RELOAD", "False")) == "True"
UVICORN_ENTRYPOINT = str(os.environ["UVICORN_ENTRYPOINT"])

# Proxy
PROXY_HOST = str(os.environ.get("PROXY_HOST", "localhost"))

# Database
DATABASE_ECHO = os.environ.get("DATABASE_ECHO", "True") == "True"

# Log
LOG_LEVEL = str(os.environ.get("LOG_LEVEL", "INFO")).upper()

# Notify
TELEGRAM_API_TOKEN = str(os.environ.get("TELEGRAM_API_TOKEN"))
TELEGRAM_CHAT_ID = int(os.environ.get("TELEGRAM_CHAT_ID", 0))