from loguru import logger
from concurrent import futures

import grpc

from blog.service import BlogService
from generated import blog_pb2_grpc

def serve():
    logger.info("Starting gRPC server")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    blog_pb2_grpc.add_BlogServiceServicer_to_server(BlogService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()