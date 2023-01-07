import os

from dotenv import load_dotenv

from {{ cookiecutter.project_module }}.paths import ENV_FILE

# --- Load Environment
load_dotenv(dotenv_path=ENV_FILE)

# --- Bind Environment variables
# Server
SERVER_IP = str(os.environ.get("SERVER_IP", "0.0.0.0"))
SERVER_PORT = int(os.environ.get("SERVER_PORT", 5000))
BASE_DOMAIN = str(os.environ.get("BASE_DOMAIN", f"{SERVER_IP}:{SERVER_PORT}"))
BASE_URL = str(os.environ.get("BASE_URL", f"http://{BASE_DOMAIN}"))
PROXY_HOST = str(os.environ.get("PROXY_HOST", "localhost"))

# Database
DATABASE_ECHO = os.environ.get("DATABASE_ECHO", "True") == "True"
