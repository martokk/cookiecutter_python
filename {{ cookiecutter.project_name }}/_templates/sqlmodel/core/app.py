from {{ cookiecutter.project_module }}.core.logger import logger
from {{ cookiecutter.project_module }}.core.notify import notify
from {{ cookiecutter.project_module }}.db.database import create_db_and_tables


async def app() -> None:
    create_db_and_tables()
    logger.info("Created database & tables.")
    print("Hello World")
    await notify(text=f"{PACKAGE_NAME}('{ENV_NAME}') started.")


if __name__ == "__main__":
    app()
