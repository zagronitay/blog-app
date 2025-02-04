from loguru import logger
from typing import List

import grpc

from api.models import CreatePostRequest, PostResponse
from contracts.generated.blog_pb2 import GetPostRequest, ListPostsRequest, Post, CreatePostRequest as GrpcCreatePostRequest
from contracts.generated.blog_pb2_grpc import BlogServiceStub


class BlogClient:
    def __init__(self, host: str = "0.0.0.0", port: int = 50051):
        channel = grpc.insecure_channel(f"{host}:{port}")
        self.client = BlogServiceStub(channel)

    def create_post(self, request: CreatePostRequest) -> PostResponse:
        grpc_request = GrpcCreatePostRequest(
            title=request.title,
            content=request.content,
            author=request.author
        )
        logger.info(f"Creating post: {grpc_request}")
        response = self.client.CreatePost(grpc_request)
        return self._post_to_response(response)

    def get_post(self, post_id: str) -> PostResponse:
        response = self.client.GetPost(GetPostRequest(id=post_id))
        return self._post_to_response(response)

    def list_posts(self, page: int = 1, page_size: int = 10) -> tuple[List[PostResponse], int]:
        response = self.client.ListPosts(
            ListPostsRequest(page=page, page_size=page_size)
        )
        posts = [self._post_to_response(post) for post in response.posts]
        return posts, response.total

    def _post_to_response(self, post: Post) -> PostResponse:
        return PostResponse(
            id=post.id,
            title=post.title,
            content=post.content,
            author=post.author,
            created_at=post.created_at
        )