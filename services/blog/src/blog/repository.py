from typing import List, Optional
import uuid
from datetime import datetime
from blog.models import PostModel, CreatePostModel


class BlogRepository:
    def __init__(self):
        self.posts = {}

    def create_post(self, post: CreatePostModel) -> PostModel:
        post_id = str(uuid.uuid4())
        new_post = PostModel(
            id=post_id,
            title=post.title,
            content=post.content,
            author=post.author,
            created_at=datetime.utcnow()
        )
        self.posts[post_id] = new_post
        return new_post

    def get_post(self, post_id: str) -> Optional[PostModel]:
        return self.posts.get(post_id)

    def list_posts(self, page: int = 1, page_size: int = 10) -> tuple[List[PostModel], int]:
        start_idx = (page - 1) * page_size
        end_idx = start_idx + page_size
        posts_list = list(self.posts.values())
        return posts_list[start_idx:end_idx], len(posts_list)