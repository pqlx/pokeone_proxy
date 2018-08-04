from typing import *
import sys
from UI.widgets import Ui_MainWindow
from UI.Startup import Startup
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QHeaderView, QTableWidgetItem
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from datetime import datetime
import json

from packet.Packet import Packet
from packet.PacketContext import PacketContext, ServerType, TransferType

class MainUI(QMainWindow):
    """
    Main UI widget
    """

    def __init__(self):
        self.app = Startup(sys.argv)
        super(MainUI, self).__init__()

        self.packets = []
        self.selected_packet = -1

    def setup(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.startup_ui()
        
    def startup_ui(self):
        self.ui.proxy_history_table.horizontalHeader().setVisible(True)
        self.ui.proxy_history_table.resizeRowsToContents()

        for n in (1, 2, 4, 5, 6):
            self.ui.proxy_history_table.horizontalHeader().setSectionResizeMode(n, QHeaderView.Stretch);
        
    def run(self, startup: Optional[Callable]):
        if startup:
            
            self.app.set_signal(lambda: startup(self))

            self.ui.proxy_history_table.cellActivated.connect(self.table_select)
            self.ui.proxy_history_table.cellClicked.connect(self.table_select)
            self.show()
            self.app.exec_()

    def table_select(self, x, y):
        if x == self.selected_packet:
            return
        self.selected_packet = x 

        self.ui.proxy_packet_edit.document().setPlainText(
            json.dumps(
                self.packets[x].proto, 
                indent=4, 
                separators=(',', ': ')
            )
        )
    
    def add_packet(self, packet: Packet):
        """
        Add a packet entry to the table
        """

        self.packets.append(packet)

        table = self.ui.proxy_history_table

        table.insertRow(table.rowCount())

        def add_to_current_row(column: int, data: str):

            widget = QTableWidgetItem(data)

            if packet.proto == False:
                widget.setBackground(QColor(255, 0, 0))

            table.setItem(
                table.rowCount() - 1,
                column,
                widget
            )

        rowdata = {
            0: str(table.rowCount()),
            1: "Game Server",
            2: datetime.now().strftime('%H:%M:%S'),
            3: "UP" if packet.ctx.transfer == TransferType.REQUEST else "Down",
            4: packet.grain,
            5: packet.ctx.local_authority,
            6: packet.ctx.remote_authority,
        }

        for k, v in rowdata.items():
            add_to_current_row(k, v)

        
        