from typing import *
from UI.MainUI import MainUI
from packet.Packet import Packet
import json
from datetime import datetime
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.Qt import QColor

from packet.PacketContext import PacketContext, TransferType, ServerType

class ProxyHistoryHandler(object):

    def __init__(self, main_window: MainUI):
        self.main_window = main_window
        self.table = main_window.ui.proxy_history_table
        self.packet_edit = self.main_window.ui.proxy_packet_edit

        self.selected_packet = -1
        self.packets = []

    
    def add_packet(self, packet: Packet):
        """
        Add a packet entry to the table
        """

        self.packets.append(packet)

        self.table.insertRow(self.table.rowCount())
        self.table.setRowHidden(self.table.rowCount() - 1, True)

        def add_to_current_row(column: int, data: str):

            widget = QTableWidgetItem(data)

            if packet.proto == False:
                widget.setBackground(QColor(255, 0, 0))

            self.table.setItem(
                self.table.rowCount() - 1,
                column,
                widget
            )

        rowdata = {
            0: str(self.table.rowCount()),
            1: "Game Server" if packet.ctx.server == ServerType.GAME else "Maps Server",
            2: packet.ctx.timestamp.strftime('%H:%M:%S'),
            3: packet.ctx.transfer.name.lower().capitalize(),
            4: packet.grain,
            5: str(packet.ctx.connection.connection_num),
            6: f"{packet.ctx.local_authority[0]}:{packet.ctx.local_authority[1]}",
            7: f"{packet.ctx.remote_authority[0]}:{packet.ctx.remote_authority[1]}"
            
        }

        for k, v in rowdata.items():
            add_to_current_row(k, v)

        self.table.setRowHidden(self.table.rowCount() - 1, False)

    def table_on_select(self, x, y):
        if x == self.selected_packet:
            return
        self.selected_packet = x 

        self.packet_edit.document().setPlainText(
            json.dumps(
                self.packets[x].proto if self.packets[x].proto else self.packets[x].proto_base64, 
                indent=4, 
                ensure_ascii=False,
                separators=(',', ': ')
            ) # .encode('utf-8')
        )