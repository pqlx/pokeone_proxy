cd ./proto_definitions 
protoc --proto_path="./" --python_out=/mnt/d/code/p1_async_proxy/protos/ `find ./ -type f -name "*.proto"`
