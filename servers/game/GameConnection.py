from typing import *
from proxy.ProxyConnection import ProxyConnection
import asyncio


class GameConnection(ProxyConnection):
    """
    Specialised ProxyConnection for `GameServer`s
    """
    __slots__ = ('state')

    def __init__(self, server: 'servers.game.GameServer.GameServer', 
                stream_operators: Tuple[Tuple[asyncio.StreamReader, asyncio.StreamReader], Tuple[asyncio.StreamWriter, asyncio.StreamWriter]],
                authority: Tuple[str, int],
                connection_num: Optional[int]=None):

                super().__init__(
                    server=server, 
                    stream_operators=stream_operators,
                    authority=authority,
                    connection_num=connection_num)
                
               # TODO add game connection specific code