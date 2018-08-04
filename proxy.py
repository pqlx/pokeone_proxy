from typing import *
import sys
import asyncio
import traceback

from PyQt5.QtWidgets import QTableWidget

class ProxyServer(object):
    __slots__ = ('loop', 'addr', 'connections', 'localhost')

    def __init__(self, loop=None):
        self.loop = loop or asyncio.get_event_loop()
        self.connections = []

    async def handle_send(self, packet: bytes) -> bytes:
        return packet

    async def handle_recv(self, packet: bytes) -> bytes:
        return packet

    async def read_packet(self, reader: asyncio.StreamReader) -> bytes:
        return await reader.readline()

    def start(self, host: str, port: int, localhost: str="0.0.0.0"):
        self.addr = (host, port)
        self.localhost = localhost
        return asyncio.start_server(self.on_client, localhost, port, loop=self.loop)
        
    async def on_client(self, client_reader: asyncio.StreamReader, client_writer: asyncio.StreamWriter):
        try:
            server_reader, server_writer = await asyncio.open_connection(*self.addr, loop=self.loop)

            connection = ProxyConnection(self, stream_operators=((server_reader, client_reader), (server_writer, client_writer)) )

            connection.pipe_streams()

            self.connections.append(connection)

            print("Client connected")
        except Exception as ex:
            print(traceback.format_exc())
            client_writer.close()

class ProxyConnection(object):
    __slots__ = ('server', 'is_closed', 'streams', 'loop')
    
    def __init__(self, server: ProxyServer, stream_operators: Tuple[Tuple[asyncio.StreamReader, asyncio.StreamReader], Tuple[asyncio.StreamWriter, asyncio.StreamWriter]] ):
        self.server = server
        self.is_closed = False
        self.streams = stream_operators

        self.loop = server.loop
        
    def close(self, writer: asyncio.StreamWriter):
        self.is_closed = True
        writer.close()

    def pipe_streams(self):
        self.loop.create_task(self._pipe(self.streams[0][0], self.streams[1][1], self.server.handle_recv))
        self.loop.create_task(self._pipe(self.streams[0][1], self.streams[1][0], self.server.handle_send))

    async def _pipe(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter, handler: Callable[[bytes], Awaitable]):
        try:
            while True:
                packet = await self.server.read_packet(reader)

                if packet == b'': # EOF
                    self.close(writer)
                    return None

                await self.send(packet, handler, writer)
        except Exception as exc:
            if not self.is_closed:
                print(f"[x] {writer.get_extra_info('perrname')} error: {traceback.format_exc()}", file=sys.stderr)
            else:
                traceback.print_exc()
        self.close(writer)
    
    async def send(packet: bytes, handler: Awaitable, writer: asyncio.StreamWriter):
        packet = await handler(bytes)
        writer.write(packet)
        await writer.drain()
    
    async def send_client(packet: bytes):
        await self.send(packet, self.server.handle_recv, self.streams[1][1])

    async def send_server(packet: bytes):
        await self.send(packet, self.server.handle_recv, self.streams[1][0])
        