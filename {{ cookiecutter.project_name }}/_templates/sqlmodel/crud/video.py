from sqlmodel import Session

from {{ cookiecutter.project_module }}.db.database import engine
from {{ cookiecutter.project_module }}.models.video import Video, VideoCreate, VideoRead

from .base import BaseCRUD


class VideoCRUD(BaseCRUD[Video, VideoCreate, VideoRead]):
    def __init__(self, session: Session) -> None:
        super().__init__(model=Video, session=session)


with Session(engine) as _session:
    video_crud = VideoCRUD(session=_session)
