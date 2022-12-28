import os

from dotenv import load_dotenv
from {{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}.paths import ENV_FILE

# --- Load Environment
load_dotenv(dotenv_path=ENV_FILE)

# --- Bind Environment variables

# Category
CONFIGURATION_VARIABLE_1 = str(os.environ.get("CONFIGURATION_VARIABLE_1", "default"))
