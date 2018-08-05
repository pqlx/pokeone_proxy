mkdir -p ./protos
cd ./proto_definitions 
protoc --proto_path="./" --python_out=../ `find ./ -type f -name "*.proto"`
find ../protos -type d -exec touch {}/__init__.py \;
