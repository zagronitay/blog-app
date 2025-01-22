from pydantic import BaseModel

class PostResponse(BaseModel):
    id: str
    title: str
    content: str
    author: str
    created_at: str

class CreatePostRequest(BaseModel):
    title: str
    content: str
    author: str