#!/usr/bin/env bash

python -m grpc_tools.protoc -Igenerated=src/protoc \
    --python_out=./src \
    --pyi_out=./src \
    --grpc_python_out=./src \
    ./src/protoc/*.proto
