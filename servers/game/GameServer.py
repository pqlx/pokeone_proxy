from typing import *
from proxy.ProxyServer import ProxyServer
from proxy.ProxyConnection import ProxyConnection
from packet.Packet import Packet
from packet.PacketContext import PacketContext, TransferType, ServerType
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QMainWindow
from PyQt5.Qt import QColor
from datetime import datetime
from UI.MainUI import MainUI
from servers.ServerSelector import ServerSelector
from packet.PacketContext import ServerType
from servers.game.GameConnection import GameConnection

import asyncio

class GameServer(ProxyServer):

    associated_connection = GameConnection # For packet stack
    servertype = ServerType.GAME

    def __init__(self, loop: Optional[asyncio.AbstractEventLoop]=None, window: Optional[MainUI]=None):
        super().__init__(loop=loop)
        self.window = window

        self.request_stack = []

    @property
    def authority(self) -> Tuple[str, int]:
        return ServerSelector.select_server(ServerType.GAME), 2012

    async def handle_request(self, connection: GameConnection, packet: bytes):
        """ Intercept client -> server """
        # data = packet_decode(packet, 'game', False)
        # ... do stuff with data
        # ... convert data back into bytes
        
        ctx = PacketContext(
            connection=connection,
            transfer=TransferType.REQUEST
        )
        
        new_packet = Packet(packet, ctx)

        

        self.add_packet_to_table(new_packet)

        return packet

    async def handle_response(self, connection: GameConnection, packet: bytes):
        """ Intercept server -> client """
        # data = packet_decode(packet, 'game', True)
        # ... do stuff with data
        # ... convert data back into bytes

        ctx = PacketContext(
            connection=connection,
            transfer=TransferType.RESPONSE
        )

        new_packet = Packet(packet, ctx)

        self.add_packet_to_table(new_packet)

        return packet

    async def read_packet(self, reader: asyncio.StreamReader) -> bytes:
        # Since packets are composed like:
        # <Grain> <Space character ' '> <optional Base64 encoded protobuf> <Carry return character '\r'> <New line character '\n'>
        # It is sufficient to read a line from the stream to get a single packet

        return await reader.readline()
    
    def add_packet_to_table(self, packet: Packet):
        if self.window:
            self.window.proxy_history_handler.add_packet(packet)