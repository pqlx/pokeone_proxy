from typing import *
from packet.Packet import Packet
from packet.PacketContext import PacketContext, ServerType, TransferType


class GrainState(object):
    """
    A class to maintain the state of packets from a server.
    The PokeOne protocol has different protobufs associated with grains depending on the context that the packet is in.
    If a `Request` packet is sent first by the client, the packet sent from the server with the same grain is treated as a `Response`.
    
    However, if no `Request` packet has been sent (i.e the server sends us packets without being prompted by the client), 
    it is instead treated as a `Payload`. A different protobuf should be selected to decode in this case, and thus a new
    field in the packet context should be added.
    """

    def __init__(self, connection: 'servers.game.GameServer.GameServer'):
        self.connection = connection

        self.state = {}

        # These grains are special and no payload exists for them, even though the server sends them without a prompt
        self.special_grains = ["Greeting", "DebugMessage"]
        
    def add(self, grain: str):

        if not grain in self.state:
            self.state[grain] = 0
        self.state[grain] += 1

    def remove(self, grain: str) -> bool:
        if not grain in self.state or self.state[grain] == 0:
            if grain in self.special_grains:
                return True
            return False
        
        self.state[grain] -= 1
        return True
