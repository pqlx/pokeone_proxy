from typing import *
import sys
import asyncio
import traceback
from proxy.ProxyConnection import ProxyConnection
from PyQt5.QtWidgets import QTableWidget

class ProxyServer(object):
    
    """
    Server that listens for connections and creates `ProxyConnection`s
    that connects all the streams of the connection, for every connection.

    This class is meant to be subclassed
    """
    
    __slots__ = ('loop', 'addr', 'connections', 'localhost')

    associated_connection = ProxyConnection # Can optionally be overridden with a subclass

    def __init__(self, loop=None):
        self.loop = loop or asyncio.get_event_loop()
        self.connections = []

    @property
    def authority(self) -> Tuple[str, int]:
        """
        Return an authority to connect to (host : port pair).

        Meant to be overriden.
        """

        return ('', 0000)

    async def handle_request(self, connection: ProxyConnection, packet: bytes) -> bytes:
        """
        Operate on packet received from the client before forwarding it to the server

        Meant to be overridden.
        """
        return packet

    async def handle_response(self, connection: ProxyConnection, packet: bytes) -> bytes:
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

    def start(self, port: int, localhost: str="0.0.0.0"):
        """
        Start listening for new clients
        """
        
        self.listening_authority = (localhost, port)
        self.localhost = localhost
        return asyncio.start_server(self.on_client, localhost, port, loop=self.loop)
        
    async def on_client(self, client_reader: asyncio.StreamReader, client_writer: asyncio.StreamWriter):
        
        """
        Create a new ProxyConnection on a new connection from a client
        """

        try:
            authority = self.authority

            server_reader, server_writer = await asyncio.open_connection(*authority, loop=self.loop)

            connection = self.associated_connection(self, 
                stream_operators=((server_reader, client_reader), (server_writer, client_writer)),
                authority=authority )

            self.connections.append(connection)

            print("Client connected")
        except Exception as ex:
            print(traceback.format_exc())
            client_writer.close()