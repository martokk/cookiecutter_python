from typing import List

from fastapi import APIRouter, HTTPException, status

from {{ cookiecutter.__project_module }}.db.crud import {{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }}_crud
from {{ cookiecutter.__project_module }}.models.{{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }} import {{ cookiecutter.fastapi_sqlmodel_template_model_name.title().replace(' ', '').replace('-', '') }}

router = APIRouter()
crud = {{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }}_crud


@router.get("/", response_model=List[{{ cookiecutter.fastapi_sqlmodel_template_model_name.title().replace(' ', '').replace('-', '') }}], status_code=status.HTTP_200_OK)
async def get_all() -> List[{{ cookiecutter.fastapi_sqlmodel_template_model_name.title().replace(' ', '').replace('-', '') }}]:
    """
    Get all items.
    """
    return crud.get_all()


@router.post("/", response_model={{ cookiecutter.fastapi_sqlmodel_template_model_name.title().replace(' ', '').replace('-', '') }}, status_code=status.HTTP_201_CREATED)
async def create({{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }}: {{ cookiecutter.fastapi_sqlmodel_template_model_name.title().replace(' ', '').replace('-', '') }}) -> {{ cookiecutter.fastapi_sqlmodel_template_model_name.title().replace(' ', '').replace('-', '') }}:
    """
    Create new item.
    """
    return crud.create({{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }})


@router.get("/{{ "{" + cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }}_id}", response_model={{ cookiecutter.fastapi_sqlmodel_template_model_name.title().replace(' ', '').replace('-', '') }})
async def get({{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }}_id: str) -> {{ cookiecutter.fastapi_sqlmodel_template_model_name.title().replace(' ', '').replace('-', '') }}:
    """
    Get item by ID.
    """
    db_{{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }} = crud.get({{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }}_id={{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }}_id)
    if db_{{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }} is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="{{ cookiecutter.fastapi_sqlmodel_template_model_name.title().replace(' ', '').replace('-', '') }} Not Found")
    return db_{{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }}


@router.patch("/{{ "{" +  cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }}_id}", response_model={{ cookiecutter.fastapi_sqlmodel_template_model_name.title().replace(' ', '').replace('-', '') }})
async def update({{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }}_id: str, {{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }}: {{ cookiecutter.fastapi_sqlmodel_template_model_name.title().replace(' ', '').replace('-', '') }}) -> {{ cookiecutter.fastapi_sqlmodel_template_model_name.title().replace(' ', '').replace('-', '') }}:
    """
    Update an item.
    """
    db_{{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }} = crud.get({{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }}_id={{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }}_id)
    if db_{{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }} is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="{{ cookiecutter.fastapi_sqlmodel_template_model_name.title().replace(' ', '').replace('-', '') }} Not Found")
    update_data = {{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }}.dict()
    for field in {{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }}.dict():
        if field in update_data:
            setattr(db_{{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }}, field, update_data[field])
    crud.update(db_{{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }})
    return {{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }}


@router.delete("/{{ "{" +  cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }}_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete({{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }}_id: str) -> bool:
    """
    Delete an item.
    """
    db_{{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }} = crud.get({{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }}_id={{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }}_id)
    if db_{{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }} is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="{{ cookiecutter.fastapi_sqlmodel_template_model_name.title().replace(' ', '').replace('-', '') }} Not Found")
    return crud.delete(db_{{ cookiecutter.fastapi_sqlmodel_template_model_name.lower().replace(' ', '_').replace('-', '_') }})
