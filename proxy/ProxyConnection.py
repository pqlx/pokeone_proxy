from typing import *
import asyncio
import traceback
from proxy.ProxyServer import ProxyServer

import sys

class ProxyConnection(object):
    
    """
    Class to describe a connections between the client and the server.
    Exposes the `asyncio.StreamReader`s and `asyncio.StreamWriter`s of both the client and the server.
    """

    __slots__ = ('server', 'is_closed', 'streams', 'loop')
    
    def __init__(self, server: ProxyServer, stream_operators: Tuple[Tuple[asyncio.StreamReader, asyncio.StreamReader], Tuple[asyncio.StreamWriter, asyncio.StreamWriter]] ):
        self.server = server
        self.is_closed = False
        self.streams = stream_operators

        self.loop = server.loop

        self.pipe_streams()
        
    def close(self):
        self.is_closed = True
        
        for writer in self.streams[1]:
            writer.close()
        
        # TODO
        # Add code to handle disconnect

    def pipe_streams(self):
        """
        Forward client_reader -> server_writer
                server_reader -> client_writer
        """
        self.loop.create_task(self._pipe(self.streams[0][0], self.streams[1][1], self.server.handle_recv))
        self.loop.create_task(self._pipe(self.streams[0][1], self.streams[1][0], self.server.handle_send))

    async def _pipe(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter, handler: Callable[[bytes], Awaitable]):
        """
        Hook up the reader to the writer, forwarding the data read in by the reader, 
        and sending it to the writer after it has been processed by the intermediary handler
        """
        try:
            while True:
                packet = await self.server.read_packet(reader)

                if packet == b'': # EOF
                    self.close()
                    return None

                await self.send(packet, handler, writer)
        except Exception as exc:
            if not self.is_closed:
                print(f"[x] {writer.get_extra_info('perrname')} error: {traceback.format_exc()}", file=sys.stderr)
            else:
                traceback.print_exc()
        self.close()
    
    async def send(self, packet: bytes, handler: Awaitable, writer: asyncio.StreamWriter):
        """
        Send data to writer after processing it with the intermediary handler
        """

        packet = await handler(packet)
        writer.write(packet)
        await writer.drain()
    
    async def send_client(packet: bytes):
        """
        Send packet to client
        """

        await self.send(packet, self.server.handle_recv, self.streams[1][1])

    async def send_server(packet: bytes):
        """
        Send packet to server
        """

        await self.send(packet, self.server.handle_recv, self.streams[1][0])
        