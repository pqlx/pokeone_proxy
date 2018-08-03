cd proto_definitions/game/PSXAPI.Request
protoc --proto_path=../../ --proto_path="./" --python_out=../../../protos/game/request *.proto
cd ../PSXAPI.Response
protoc --proto_path=../../ --proto_path="./" --python_out=../../../protos/game/response/ *.proto
cd ../PSXAPI.Response.Payload
protoc --proto_path=../../ --proto_path="./" --python_out=../../../protos/game/response/payload *.proto
cd ../../maps/MAPAPI.Request
protoc --proto_path=../../ --proto_path="./" --python_out=../../../protos/maps/request/ *.proto
cd ../MAPAPI.Response
protoc --proto_path=../../ --proto_path="./" --python_out=../../../protos/maps/response *.proto
