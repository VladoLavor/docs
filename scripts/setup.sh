#!/usr/bin/env bash

curl -OL https://github.com/google/protobuf/releases/download/v3.2.0/protoc-3.2.0-linux-x86_64.zip
unzip protoc-3.2.0-linux-x86_64.zip -d protoc3
cp protoc3/bin/* /usr/local/bin/
cp protoc3/include/* /usr/local/include/