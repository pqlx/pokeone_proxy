from typing import *
from proxy import ProxyServer
from packetparser import packet_decode
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QMainWindow
from PyQt5.Qt import QColor
from datetime import datetime

class GameServer(ProxyServer):

    def __init__(self, loop=None, window: QMainWindow=None):
        super().__init__(loop=loop)
        self.window = window

        self.table = window.ui.proxy_history_table

    async def handle_send(self, packet: bytes):
        """ Intercept client -> proxy """
        # data = packet_decode(data, 'game', False)
        # ... do stuff with data
        # ... convert data back into bytes
        
        grain, decoded = packet_decode(packet, 'game', False)
        
        self.add_table_entry(grain, packet, decoded, False)

        return packet

    async def handle_recv(self, packet: bytes):
        """ Intercept proxy -> client """
        # data = packet_decode(data, 'game', True)
        # ... do stuff with data
        # ... convert data back into bytes

        grain, decoded = packet_decode(packet, 'game', True)

        print(decoded)
        self.add_table_entry(grain, packet, decoded, True)

        return packet

    def add_table_entry(self, grain: str, original_packet: bytes, decoded_packet: dict, receiving: bool):
        
        def remove_bytes_dict(element):
            if type(element) == list:
                for i in range(len(element)):
                    element[i] = remove_bytes_dict(element[i])
                return element
            if type(element) == dict:
                for key in element.keys():
                    element[key] = remove_bytes_dict(element[key])
                return element            
            elif type(element) == bytes:
                try:
                    return element.decode('utf-8')
                except UnicodeDecodeError:
                    return "< Could not decode bytes >"
            return element

        remove_bytes_dict(decoded_packet)

        if self.window.packets != None:
            
            packet_data = {
                "grain": grain,
                "data": decoded_packet,
                
            }
            if packet_data["data"] in [False, None]:
                packet_data["original"] = original_packet.decode('utf-8').strip()

            print(f"Appended {grain}")  
            self.window.packets.append(packet_data)

            self.table.insertRow(self.table.rowCount())

            def add_to_current_row(column: int, data: str):

                widget = QTableWidgetItem(data)

                if packet_data["data"] in [False, None]:
                    widget.setBackground(QColor(255, 0, 0))

                self.table.setItem(
                    self.table.rowCount() - 1,
                    column,
                    widget
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
        
