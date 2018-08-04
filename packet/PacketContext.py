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
    __slots__ = ("server", "transfer", "remote_host", "local_host", "port")

    def __init__(self, server: Optional[ServerType]=None, transfer: Optional[TransferType]=None, 
                 remote_host: Optional[str]=None, local_host: Optional[str]=None, 
                 port: Optional[int]=None):
        self.server = server
        self.transfer = transfer
        self.remote_host = remote_host
        self.local_host = local_host
        self.port = port
    
    @property
    def path(self) -> str:
        """
        Return context as path, i.e game.request, or maps.response
        """
        path = '.'.join([getattr(x, 'name') for x in [self.server, self.transfer] ])
        
        return path.lower()
    
    @property
    def local_authority(self) -> str:
        return f"{self.local_host}:{self.port}"

    @property
    def remote_authority(self) -> str:
        return f"{self.remote_host}:{self.port}"