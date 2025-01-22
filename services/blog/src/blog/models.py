from datetime import datetime
from pydantic import BaseModel


class PostModel(BaseModel):
    id: str
    title: str
    content: str
    author: str
    created_at: datetime


class CreatePostModel(BaseModel):
    title: str
    content: str
    author: str