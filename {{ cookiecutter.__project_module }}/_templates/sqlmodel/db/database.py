from loguru import logger
from sqlmodel import SQLModel, create_engine

from {{ cookiecutter.__project_module }}.config import DATABASE_ECHO
from {{ cookiecutter.__project_module }}.paths import DATABASE_FILE

database_url = f"sqlite:///{DATABASE_FILE}"

connect_args = {"check_same_thread": False}
engine = create_engine(database_url, echo=DATABASE_ECHO, connect_args=connect_args)


async def create_db_and_tables() -> None:
    """Creates all SQLModel databases if not already created."""
    logger.info("Creating database tables")
    SQLModel.metadata.create_all(engine)
