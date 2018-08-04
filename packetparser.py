from typing import *
from base64 import b64decode
from importlib import import_module
from google.protobuf.json_format import MessageToDict, MessageToJson

import traceback

def packet_decode(encoded_packet: bytes, server: str, receiving: bool, payload: bool=False) -> Tuple[str, Union[bool, dict]]:
    
    packet = encoded_packet.decode()

    if server != "game":
        server = "maps"
    
    try:
        grain, data = tuple(map(lambda s: s.rstrip(), packet.split(' ')))
    except ValueError:
        # Incorrect format
        return '', False
    
    if '.' in grain:
        return grain, False
    
    folder = '.'.join([server, ['request', 'response'][int(receiving)]])
    if payload:
        folder += '.payload'

    try:
        deserializer = getattr(import_module(f'protos.{folder}.{grain}_pb2'), grain)()
        deserializer.ParseFromString(b64decode(data))
        return grain, MessageToDict(deserializer)
    except Exception as exc:
        
        if receiving and server == "game":
            # Does not seem to work
            return packet_decode(encoded_packet, server, receiving, payload=True)
            
        print(traceback.print_exc())
        # Failed deserializing proto
        return grain, False

def packet_encode():
    pass