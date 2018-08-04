from typing import *
from proxy.ProxyServer import ProxyServer
from packet.Packet import Packet
from packet.PacketContext import PacketContext, TransferType, ServerType
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QMainWindow
from PyQt5.Qt import QColor
from datetime import datetime
from UI.MainUI import MainUI

import asyncio


class GameServer(ProxyServer):

    def __init__(self, loop: Optional[asyncio.AbstractEventLoop]=None, window: Optional[MainUI]=None):
        super().__init__(loop=loop)
        self.window = window

        if window:
            self.table = window.ui.proxy_history_table

    async def handle_send(self, packet: bytes):
        """ Intercept client -> server """
        # data = packet_decode(packet, 'game', False)
        # ... do stuff with data
        # ... convert data back into bytes
        
        
        ctx = PacketContext(ServerType.GAME, TransferType.REQUEST)
        
        new_packet = Packet(packet, ctx)

        print(new_packet.proto)

        self.add_packet_to_table(new_packet)

        return packet

    async def handle_recv(self, packet: bytes):
        """ Intercept server -> client """
        # data = packet_decode(packet, 'game', True)
        # ... do stuff with data
        # ... convert data back into bytes

        ctx = PacketContext(ServerType.GAME, TransferType.RESPONSE)

        new_packet = Packet(packet, ctx)

        self.add_packet_to_table(new_packet)

        return packet

    async def read_packet(self, reader: asyncio.StreamReader) -> bytes:
        # Since packets are composed like:
        # <Grain> <Space character ' '> <Base64 encoded protobuf> <Carry return character '\r'> <New line character '\n'>
        # It is sufficient to read a line from the stream to get a single packet

        return await reader.readline()
    
    def add_packet_to_table(self, packet: Packet):
        if self.window:
            self.window.add_packet(packet)