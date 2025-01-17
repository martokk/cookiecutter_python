from fastapi import APIRouter, HTTPException, status

from {{ cookiecutter.project_module }}.crud.exceptions import RecordAlreadyExistsError, RecordNotFoundError
from {{ cookiecutter.project_module }}.crud.video import video_crud
from {{ cookiecutter.project_module }}.models.video import Video, VideoCreate, VideoRead

router = APIRouter()
crud = video_crud
ModelClass = Video
ModelReadClass = VideoRead
ModelCreateClass = VideoCreate


@router.post("/", response_model=ModelReadClass, status_code=status.HTTP_201_CREATED)
async def create(in_obj: ModelClass) -> ModelClass:
    """
    Create a new item.
    """
    try:
        return await crud.create(in_obj=in_obj)
    except RecordAlreadyExistsError as exc:
        raise HTTPException(status_code=status.HTTP_200_OK, detail="Video already exists") from exc


@router.get("/{id}", response_model=ModelReadClass)
async def get(id: str) -> ModelClass | None:
    """
    Get an item.
    """
    try:
        return await crud.get(id=id)
    except RecordNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Video Not Found"
        ) from exc


@router.get("/", response_model=list[ModelReadClass], status_code=status.HTTP_200_OK)
async def get_all() -> list[ModelClass] | None:
    """
    Get all items.
    """
    return await crud.get_all()


@router.patch("/{id}", response_model=ModelReadClass)
async def update(id: str, in_obj: ModelCreateClass) -> ModelClass:
    """
    Update an item.
    """
    try:
        return await crud.update(in_obj, id=id)
    except RecordNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Video Not Found"
        ) from exc


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: str) -> None:
    """
    Delete an item.
    """
    try:
        return await crud.delete(id=id)
    except RecordNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Video Not Found"
        ) from exc
