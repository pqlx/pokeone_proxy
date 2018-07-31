from typing import *

import sys
import asyncio

import traceback

class ProxyServer(object):
    __slots__ = ('loop', 'proxy')

    def __init__(self, loop=None):
        self.loop = loop or asyncio.get_event_loop()

    def start(self, host: str, port: int, local_host: str="0.0.0.0") -> Awaitable:
        self.proxy = (host, port)
        return asyncio.start_server(self.__handle__, local_host, port, loop=self.loop)

    async def handle_send(self, packet: bytes) -> bytes:
        return packet

    async def handle_recv(self, packet: bytes) -> bytes:
        return packet
    
    async def __connect__(self) -> Optional[Tuple[asyncio.StreamReader, asyncio.StreamWriter]]:
        try:
            return await asyncio.open_connection(*self.proxy, loop=self.loop)
        except Exception as exc:
            print(f'Failed to create connection to proxy:', file=sys.stderr)
            return None

    async def __handle__(self, client_reader: asyncio.StreamReader, client_writer: asyncio.StreamWriter) -> None:
        proxy_connection = await self.__connect__()
        if not proxy_connection:
            return client_writer.close()
        proxy_reader, proxy_writer = proxy_connection

        while True:
            try:
                packet = await self.read_packet(client_reader)
                print(packet)
                proxy_writer.write(self.handle_send(packet))
                proxy_writer.drain()

                packet = await self.read_packet(proxy_reader)
                client_writer.write(self.handle_recv(packet))
                client_writer.drain()
            except Exception as exc:
                print(f'Client closed with exception: {exc} \n\n{traceback.format_exc()}', file=sys.stderr)
                break

        proxy_writer.close()
        client_writer.close()

    async def read_packet(self, reader: asyncio.StreamReader) -> bytes:
        return reader.readline()
