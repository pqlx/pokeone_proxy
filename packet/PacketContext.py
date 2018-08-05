from typing import *
from enum import Enum
from datetime import datetime

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
    PAYLOAD = 2


class PacketContext(object):
    """
    Class to give context about a packet
    """
    __slots__ = ("server",
                 "transfer",
                 "remote_authority",
                 "local_authority",
                 "is_payload_response",
                 "timestamp")

    def __init__(self, 
                 server: Optional[ServerType]=None,
                 transfer: Optional[TransferType]=None,
                 remote_authority: Tuple[Optional[str], Optional[int]]=(None, None),
                 local_authority: Tuple[Optional[str], Optional[int]]=(None, None),
                 ):
        self.server = server
        self.transfer = transfer
        self.remote_authority = remote_authority
        self.local_authority = local_authority

        self.timestamp = datetime.now()
    
    @property
    def path(self) -> str:
        """
        Return context as path, i.e game.request, or maps.response
        """
        path = '.'.join([getattr(x, 'name') for x in [self.server, self.transfer] ])
        
        return path.lower()