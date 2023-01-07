from typing import Any

import datetime

from dateutil import tz
from pydantic import root_validator
from sqlmodel import Field, SQLModel

# if TYPE_CHECKING:
#     from {{ cookiecutter.project_module }}.models.source import Source


class VideoBase(SQLModel):
    id: str = Field(default=None, primary_key=True, nullable=False)
    uploader: str = Field(default=None)
    uploader_id: str = Field(default=None)
    title: str = Field(default=None)
    description: str = Field(default=None)
    duration: int = Field(default=None)
    thumbnail: str = Field(default=None)
    url: str = Field(default=None)
    added_at: datetime.datetime = Field(default=None)
    updated_at: datetime.datetime = Field(default=None)


class Video(VideoBase, table=True):
    # source_id: str = Field(default=None, foreign_key="source.id")
    # source: "Source" = Relationship(back_populates="videos")

    @root_validator(pre=True)
    def set_pre_validation_defaults(cls, values: dict[str, Any]) -> dict[str, Any]:
        sanitized_url = values["url"]
        video_id = generate_uuid_from_url(url=sanitized_url)
        return {
            **values,
            "url": sanitized_url,
            "id": video_id,
            "updated_at": datetime.datetime.now(tz=tz.tzutc()),
        }


class VideoCreate(VideoBase):
    @root_validator
    def create_updated_at(cls, values: dict[str, Any | None]) -> dict[str, Any]:
        values["updated_at"] = datetime.datetime.now(tz=tz.tzutc())
        return values


class VideoRead(VideoBase):
    # source_id: str = Field(default=None, foreign_key="source.id")
    pass


def generate_uuid_from_url(url: str) -> str:
    return "abc123def456"
