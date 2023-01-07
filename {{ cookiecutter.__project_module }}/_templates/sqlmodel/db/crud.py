from sqlmodel import Session
from sqlmodel_basecrud import BaseRepository  # type: ignore

from {{ cookiecutter.__project_module }}.db.database import engine
from {{ cookiecutter.__project_module }}.models.{{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }} import {{ cookiecutter.fastapi_sqlmodel_template_model_name.title().replace(' ', '').replace('-', '') }}

with Session(engine) as session:
    {{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }}_crud = BaseRepository(db=session, model={{ cookiecutter.fastapi_sqlmodel_template_model_name.title().replace(' ', '').replace('-', '') }})
