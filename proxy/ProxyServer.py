from typing import *
import sys
import asyncio
import traceback

from PyQt5.QtWidgets import QTableWidget

class ProxyServer(object):
    
    """
    Server that listens for connections and creates `ProxyConnection`s
    that connects all the streams of the connection, for every connection.

    This class is meant to be subclassed
    """
    
    __slots__ = ('loop', 'addr', 'connections', 'localhost')

    def __init__(self, loop=None):
        self.loop = loop or asyncio.get_event_loop()
        self.connections = []

    async def handle_send(self, packet: bytes) -> bytes:
        """
        Operate on packet received from the client before forwarding it to the server

        Meant to be overridden.
        """
        return packet

    async def handle_recv(self, packet: bytes) -> bytes:
        """
        Operate on packet received from the server before forwarding it to the client

        Meant to be overridden.
        """
        return packet

    async def read_packet(self, reader: asyncio.StreamReader) -> bytes:
        """
        Return a single packet from the stream.

        Meant to be overridden
        """

        return b''

    def start(self, host: str, port: int, localhost: str="0.0.0.0"):
        """
        Start listening for new clients
        """
        
        self.addr = (host, port)
        self.localhost = localhost
        return asyncio.start_server(self.on_client, localhost, port, loop=self.loop)
        
    async def on_client(self, client_reader: asyncio.StreamReader, client_writer: asyncio.StreamWriter):
        
        """
        Create a new ProxyConnection on a new connection from a client
        """
        from proxy.ProxyConnection import ProxyConnection

        try:
            server_reader, server_writer = await asyncio.open_connection(*self.addr, loop=self.loop)

            connection = ProxyConnection(self, stream_operators=((server_reader, client_reader), (server_writer, client_writer)) )

            self.connections.append(connection)

            print("Client connected")
        except Exception as ex:
            print(traceback.format_exc())
            client_writer.close()