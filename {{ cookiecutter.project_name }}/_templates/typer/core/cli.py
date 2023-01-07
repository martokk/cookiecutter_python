import typer
from loguru import logger
from rich.console import Console

from {{ cookiecutter.project_module }} import version
from {{ cookiecutter.project_module }}.constants import PACKAGE_DESCRIPTION, PACKAGE_NAME
from {{ cookiecutter.project_module }}.core.server import start_server

# from {{ cookiecutter.project_module }}.core.app import app

# Configure Rich Console
console = Console()

# Configure Typer
typer_app = typer.Typer(
    name=PACKAGE_NAME,
    help=PACKAGE_DESCRIPTION,
    add_completion=False,
)


# Typer Command Callbacks
def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(f"[yellow]{PACKAGE_NAME}[/] version: [bold blue]{version}[/]")
        raise typer.Exit()


# Typer Commands
@typer_app.command()
def main(
    print_version: bool = typer.Option(  # pylint: disable=unused-argument
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the '{APP_NAME}' package.",
    ),
) -> None:
    """Main entrypoint into application"""

    # Start Uvicorn
    logger.info("Starting Server...")
    start_server()

    # OR

    # Start App
    # logger.info("Starting App...")
    # app()

    raise NotImplementedError("cli.py:main lines 43 to 52 to setup the app.")
