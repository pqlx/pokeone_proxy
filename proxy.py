from typing import *
import sys
import asyncio
import traceback

from PyQt5.QtWidgets import QTableWidget

class ProxyServer(object):
    __slots__ = ('loop', 'addr')

    def __init__(self, loop=None):
        self.loop = loop or asyncio.get_event_loop()

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
            proxy_reader, proxy_writer = await asyncio.open_connection(*self.addr, loop=self.loop)
            connection = ProxyConnection(self)
            self.loop.create_task(connection.pipe(proxy_reader, client_writer, self.handle_recv))
            self.loop.create_task(connection.pipe(client_reader, proxy_writer, self.handle_send))

            print("Client connected")
        except Exception as ex:
            print(ex)
            client_writer.close()

class ProxyConnection:
    __slots__ = ('server', 'is_closed')
    
    def __init__(self, server: ProxyServer):
        self.server = server
        self.is_closed = False

    def close(self, writer: asyncio.StreamWriter):
        self.is_closed = True
        writer.close()

    async def pipe(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter, handler: Callable[[bytes], Awaitable]):
        try:
            while True:
                packet = await self.server.read_packet(reader)

                if packet == b'': # EOF
                    self.close(writer)
                    return None

                packet = await handler(packet)
                writer.write(packet)
                await writer.drain()
        except Exception as exc:
            if not self.is_closed:
                print(f"[x] {writer.get_extra_info('perrname')} error: {traceback.format_exc()}", file=sys.stderr)
        self.close(writer)
