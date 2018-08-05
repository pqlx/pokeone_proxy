from typing import *
from proxy.ProxyConnection import ProxyConnection
from packet.GrainState import GrainState

import asyncio

class GameConnection(ProxyConnection):
    """
    A ProxyConnection with support for `PacketStack`s
    """
    __slots__ = ('packet_stack', 'state')

    def __init__(self, server: 'proxy.ProxyServer.ProxyServer', 
                stream_operators: Tuple[Tuple[asyncio.StreamReader, asyncio.StreamReader], Tuple[asyncio.StreamWriter, asyncio.StreamWriter]],
                authority: Tuple[str, int] ):

                super().__init__(
                    server, 
                    stream_operators,
                    authority)
                
                self.state = GrainState(self)