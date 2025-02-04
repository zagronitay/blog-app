#!/usr/bin/env bash

python -m grpc_tools.protoc -Icontracts/generated=src/contracts/protoc \
    --python_out=./src \
    --pyi_out=./src \
    --grpc_python_out=./src \
    ./src/contracts/protoc/*.proto
