from typing import *
from proxy import ProxyServer
from packetparser import packet_decode
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from datetime import datetime

class GameServer(ProxyServer):

    def __init__(self, loop=None, table: Optional[QTableWidget]=None, decoded_packets: list=None):
        super().__init__(loop=loop)
        self.table = table
        self.decoded_packets = decoded_packets

    async def handle_send(self, packet: bytes):
        """ Intercept client -> proxy """
        # data = packet_decode(data, 'game', False)
        # ... do stuff with data
        # ... convert data back into bytes
        
        grain, decoded = packet_decode(packet, 'game', False)
        
        self.add_table_entry(grain, decoded, False)

        return packet

    async def handle_recv(self, packet: bytes):
        """ Intercept proxy -> client """
        # data = packet_decode(data, 'game', True)
        # ... do stuff with data
        # ... convert data back into bytes

        grain, decoded = packet_decode(packet, 'game', True)

        self.add_table_entry(grain, decoded, True)

        return packet

    def add_table_entry(self, grain: str, decoded_packet: dict, receiving: bool):

        if self.decoded_packets != None:
            
            packet_data = {
                "grain": grain,
                "data": decoded_packet
            }
            print(f"Appended {grain}")
            self.decoded_packets.append(packet_data)

            self.table.insertRow(self.table.rowCount())

            def add_to_current_row(column: int, data: str):
                self.table.setItem(
                    self.table.rowCount() - 1,
                    column,
                    QTableWidgetItem(data)
                )
            
            rowdata = {
                0: str(self.table.rowCount()),
                1: "Game Server",
                2: datetime.now().strftime('%H:%M:%S'),
                3: ["UP", "DOWN"][int(receiving)],
                4: grain,
                5: f"{self.localhost}:{self.addr[1]}",
                6: f"{self.addr[0]}:{self.addr[1]}",
            }

            for k, v in rowdata.items():
                add_to_current_row(k, v)
        
