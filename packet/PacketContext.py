from typing import *
from enum import Enum


class ServerType(Enum):
    """
    Describe server type
    """
    GAME = 0
    MAPS = 1
    
class TransferType(Enum):
    """
    Describe transfer type
    """
    REQUEST = 0
    RESPONSE = 1

class PacketContext(object):
    """
    Class to give context about a packet
    """
    __slots__ = ("server", "transfer")

    def __init__(self, server: ServerType, transfer: TransferType):
        self.server = server
        self.transfer = transfer
    
    @property
    def path(self) -> str:
        """
        Return context as path, i.e game.request, or maps.response
        """
        path = '.'.join([getattr(x, 'name') for x in [self.server, self.transfer] ])
        
        return path.lower()