from loguru import logger
from {{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}.db.database import create_db_and_tables


def app() -> None:
    create_db_and_tables()
    logger.info("Created database & tables.")
    print("Hello World")


if __name__ == "__main__":
    app()
