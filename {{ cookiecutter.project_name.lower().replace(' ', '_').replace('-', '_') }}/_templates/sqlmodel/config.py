import os

from dotenv import load_dotenv
from {{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}.paths import ENV_FILE

# --- Load Environment
load_dotenv(dotenv_path=ENV_FILE)

# --- Bind Environment variables

# Database
DATABASE_ECHO = os.environ.get("DATABASE_ECHO", "True") == "True"
