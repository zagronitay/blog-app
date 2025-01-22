from loguru import logger

from fastapi import FastAPI, HTTPException
from typing import List
from api.blog import BlogClient
from api.models import CreatePostRequest, PostResponse


app = FastAPI(title="Blog API")
blog_client = BlogClient()

@app.post("/posts", response_model=PostResponse)
async def create_post(request: CreatePostRequest):
    logger.info(f"Creating post: {request}")
    try:
        return blog_client.create_post(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/posts/{post_id}", response_model=PostResponse)
async def get_post(post_id: str):
    logger.info(f"Getting post: {post_id}")
    try:
        return blog_client.get_post(post_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail="Post not found")

@app.get("/posts", response_model=List[PostResponse])
async def list_posts(page: int = 1, page_size: int = 10):
    logger.info(f"Listing posts: page={page}, page_size={page_size}")
    try:
        posts, total = blog_client.list_posts(page, page_size)
        return posts
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)