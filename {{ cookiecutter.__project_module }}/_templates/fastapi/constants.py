import os

from {{ cookiecutter.__project_module }}.config import SERVER_IP, SERVER_PORT

PACKAGE_NAME = "{{ cookiecutter.__project_module }}"
PACKAGE_DESCRIPTION = "A python project created by Martokk."
BASE_DOMAIN = str(os.environ.get("BASE_DOMAIN", f"{SERVER_IP}:{SERVER_PORT}"))
BASE_URL = str(os.environ.get("BASE_URL", f"http://{BASE_DOMAIN}"))