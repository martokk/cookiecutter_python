from {{ cookiecutter.project_module }}.core.logger import logger

from {{ cookiecutter.project_module }}.core.cli import typer_app


if __name__ == "__main__":
    logger.info(f"Starting Typer App: '{typer_app.info.name}'...")
    typer_app()
