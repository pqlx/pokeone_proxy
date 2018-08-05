from typing import *
from enum import Enum
from datetime import datetime

from servers.game.GameConnection import GameConnection

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
    __slots__ = ("connection",
                 "server",
                 "transfer",
                 "remote_authority",
                 "local_authority",
                 "timestamp")

    def __init__(self, 
                 transfer: Optional[TransferType]=None,
                 connection: Optional[GameConnection]=None
                 ):
        self.connection = connection
        self.transfer = transfer
        if connection:
            self.server = connection.server.servertype
            self.remote_authority = connection.authority
            self.local_authority = connection.server.listening_authority

        self.timestamp = datetime.now()
    
    @property
    def path(self) -> str:
        """
        Return context as path, i.e game.request, or maps.response
        """
        path = '.'.join([getattr(x, 'name') for x in [self.server, self.transfer] ])
        
        return path.lower()