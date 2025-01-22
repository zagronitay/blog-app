from loguru import logger
import grpc

from generated import blog_pb2_grpc, blog_pb2
from blog.repository import BlogRepository
from blog.models import CreatePostModel


class BlogService(blog_pb2_grpc.BlogServiceServicer):
    def __init__(self):
        self.repository = BlogRepository()

    def CreatePost(self, request, context):
        logger.info(f"Creating post {request.title}")
        post = self.repository.create_post(
            CreatePostModel(
                title=request.title,
                content=request.content,
                author=request.author
            )
        )
        return self._post_to_proto(post)

    def GetPost(self, request, context):
        logger.info(f"Getting post {request.id}")
        post = self.repository.get_post(request.id)
        if not post:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Post not found")
            return blog_pb2.Post()
        return self._post_to_proto(post)

    def ListPosts(self, request, context):
        logger.info(f"Listing posts")
        posts, total = self.repository.list_posts(
            page=request.page,
            page_size=request.page_size
        )
        response = blog_pb2.ListPostsResponse()
        response.total = total
        response.posts.extend([self._post_to_proto(post) for post in posts])
        return response

    def _post_to_proto(self, post):
        logger.info(f"Converting post {post.id} to proto")
        return blog_pb2.Post(
            id=post.id,
            title=post.title,
            content=post.content,
            author=post.author,
            created_at=post.created_at.isoformat()
        )