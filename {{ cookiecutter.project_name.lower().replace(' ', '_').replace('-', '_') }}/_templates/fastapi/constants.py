import os

from {{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}.config import SERVER_IP, SERVER_PORT

PACKAGE_NAME = "{{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}"
PACKAGE_DESCRIPTION = "A python project created by Martokk."
BASE_DOMAIN = str(os.environ.get("BASE_DOMAIN", f"http://{SERVER_IP}:{SERVER_PORT}"))
