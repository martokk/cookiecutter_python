from typing import Optional

from sqlmodel import Field, SQLModel


class {{ cookiecutter.fastapi_sqlmodel_template_model_name.title().replace(' ', '').replace('-', '') }}(SQLModel, table=True):
    {{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }}_id: str = Field(primary_key=True, nullable=False)
    field_1: str = Field()
    field_2: int = Field()
    field_3: str = Field()
    field_4: int = Field()

