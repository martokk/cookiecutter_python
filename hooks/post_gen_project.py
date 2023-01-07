"""This module is called after project is created."""
from typing import List

import shutil
import textwrap
from pathlib import Path

# Project root directory
PROJECT_DIRECTORY = Path.cwd().absolute()
PROJECT_NAME = "{{ cookiecutter.project_name }}"
PROJECT_MODULE = "{{ cookiecutter.__project_module }}"

CREATE_CONTAINER_DOCKER_TEMPLATES = "{{ cookiecutter.create_container_docker_templates }}" == "yes"
CREATE_CLI_TYPER_TEMPLATES = "{{ cookiecutter.create_cli_typer_templates }}" == "yes"
CREATE_DB_SQLMODEL_TEMPLATES = "{{ cookiecutter.create_db_sqlmodel_templates }}" == "yes"
CREATE_SERVER_FASTAPI_TEMPLATES = "{{ cookiecutter.create_server_fastapi_templates }}" == "yes"
FASTAPI_SQLMODEL_TEMPLATE_MODEL_NAME = "{{ cookiecutter.fastapi_sqlmodel_template_model_name }}"


# Values to generate correct license
LICENSE = "{{ cookiecutter.license }}"
ORGANIZATION = "{{ cookiecutter.organization }}"

# Values to generate github repository
GITHUB_USER = "{{ cookiecutter.github_name }}"

licences_dict = {
    "MIT": "mit",
    "BSD-3": "bsd3",
    "GNU GPL v3.0": "gpl3",
    "Apache Software License 2.0": "apache",
}


def generate_license(directory: Path, licence: str) -> None:
    """Generate license file for the project.

    Args:
        directory: path to the project directory
        licence: chosen licence
    """
    shutil.move(str(directory / "_licences" / f"{licence}.txt"), str(directory / "LICENSE"))
    shutil.rmtree(str(directory / "_licences"))


def generate_starter_templates(
    directory: Path,
    module_name: str,
    create_container_docker_templates: bool,
    create_cli_typer_templates: bool,
    create_db_sqlmodel_templates: bool,
    create_server_fastapi_templates: bool,
) -> None:

    # Copy Templates to Main Project Folder
    project_folder = directory
    templates_folder = project_folder / "_templates"
    module_folder = directory / module_name

    if create_container_docker_templates:
        shutil.copytree(templates_folder / "docker", project_folder, dirs_exist_ok=True)

    if create_cli_typer_templates:
        shutil.copytree(templates_folder / "typer", module_folder, dirs_exist_ok=True)

    if create_db_sqlmodel_templates:
        shutil.copytree(templates_folder / "sqlmodel", module_folder, dirs_exist_ok=True)

    if create_server_fastapi_templates:
        shutil.copytree(templates_folder / "fastapi", module_folder, dirs_exist_ok=True)

    # Copy "combination" Templates to Main Project Folder
    if create_db_sqlmodel_templates and create_server_fastapi_templates:
        shutil.copytree(templates_folder / "__fastapi_sqlmodel", module_folder, dirs_exist_ok=True)

    # Delete Templates Folder
    shutil.rmtree(templates_folder)


def print_further_instructions(project_name: str, github: str) -> None:
    """Show user what to do next after project creation.

    Args:
        project_name: current project name
        github: GitHub username
    """
    message = f"""
    Your project {project_name} is created.

    1) Now you can start working on it:

        $ cd {project_name} && git init

    2) If you don't have Poetry installed run:

        $ make poetry-download

    3) Initialize poetry and install pre-commit hooks:

        $ make install
        $ make pre-commit-install

    4) Run codestyle:

        $ make codestyle

    5) Upload initial code to GitHub:

        $ git add .
        $ git commit -m ":tada: Initial commit"
        $ git branch -M main
        $ git remote add origin https://github.com/{github}/{project_name}.git
        $ git push -u origin main
    """
    print(textwrap.dedent(message))


def main() -> None:
    generate_license(directory=PROJECT_DIRECTORY, licence=licences_dict[LICENSE])
    generate_starter_templates(
        directory=PROJECT_DIRECTORY,
        module_name=PROJECT_MODULE,
        create_container_docker_templates=CREATE_CONTAINER_DOCKER_TEMPLATES,
        create_cli_typer_templates=CREATE_CLI_TYPER_TEMPLATES,
        create_db_sqlmodel_templates=CREATE_DB_SQLMODEL_TEMPLATES,
        create_server_fastapi_templates=CREATE_SERVER_FASTAPI_TEMPLATES,
    )
    print_further_instructions(project_name=PROJECT_NAME, github=GITHUB_USER)


if __name__ == "__main__":
    main()
