from {{ cookiecutter.project_module }}.core.logger import logger
from {{ cookiecutter.project_module }}.core import app

if __name__ == "__main__":
    app()
