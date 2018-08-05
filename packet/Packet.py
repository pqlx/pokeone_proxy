from typing import *
from importlib import import_module
from google.protobuf.json_format import MessageToDict, MessageToJson
import base64
import traceback

from packet.PacketContext import PacketContext, ServerType, TransferType



class Packet(object):
    """
    Class to represent a packet
    """

    __slots__ = ("data", "ctx", "_grain", "_full_grain", "_proto", "_proto_raw", "_proto_base64")
    
    def __init__(self, data: bytes, ctx: Optional[PacketContext]=None):
        self.data = data.decode('utf-8').strip()
        self.ctx = ctx
        self._grain = None
        self._full_grain = None
        self._proto = None
        self._proto_raw = None
        self._proto_base64 = None

    @property
    def grain(self) -> str:
        if not self._grain:
           self._set_grain_and_proto_base64()
        return self._grain

    @property
    def full_grain(self) -> str:
        if not self._full_grain:
            self._full_grain = self.ctx.path + '.' + self.grain
       
        return self._full_grain

    @property
    def proto(self) -> dict:
        if self._proto is None:
            self._proto = self.decode_proto()
        return self._proto
    
    @property
    def proto_raw(self) -> bytes:
        if self._proto_raw is None:
            self._proto_raw = base64.b64decode(self.proto_base64)
        return self._proto_raw
    
    @property
    def proto_base64(self) -> str:
        if self._proto_base64 is None:
            self._set_grain_and_proto_base64()
        return self._proto_base64

    def _set_grain_and_proto_base64(self):
         split = self.data.split(' ')

         self._grain = split[0]
         if len(split) == 2:
             self._proto_base64 = split[1]
         self._grain = self._grain.replace('.', '') # Prevent potential semi-arbitrary import
        
    def decode_proto(self) -> Union[dict, bool]:
        try:
            deserializer = getattr(import_module(f'protos.{self.full_grain}_pb2'), self.grain)()
            deserializer.ParseFromString(self.proto_raw)
            return MessageToDict(deserializer)
        except Exception as exc:
            print(traceback.format_exc())
            # Failed deserializing proto
            return False

    def encode_proto() -> Union[bytes, bool]:
        pass

