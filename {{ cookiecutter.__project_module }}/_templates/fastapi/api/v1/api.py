from fastapi import APIRouter

from {{ cookiecutter.__project_module }}.api.v1.endpoints import {{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }}

api_router = APIRouter()
api_router.include_router({{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }}.router, prefix="/{{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }}", tags=["{{ cookiecutter.fastapi_sqlmodel_template_model_name.title().replace(' ', '').replace('-', '') }}"])
