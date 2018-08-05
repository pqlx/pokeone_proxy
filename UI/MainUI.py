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
        

    def setup(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.startup_ui()

        self.add_handlers()
        
    def startup_ui(self):
        self.ui.proxy_history_table.horizontalHeader().setVisible(True)
        self.ui.proxy_history_table.resizeRowsToContents()

        for n in (1, 2, 3, 4, 6, 7):
            self.ui.proxy_history_table.horizontalHeader().setSectionResizeMode(n, QHeaderView.Stretch);
        
    def run(self, startup: Optional[Callable]):
        if startup:
            
            self.app.set_signal(lambda: startup(self))

            self.ui.proxy_history_table.cellActivated.connect(self.proxy_history_handler.table_on_select)
            self.ui.proxy_history_table.cellClicked.connect(self.proxy_history_handler.table_on_select)
            self.show()
            self.app.exec_()
    
    def add_handlers(self):
        from UI.proxy.ProxyHistoryHandler import ProxyHistoryHandler
        self.proxy_history_handler = ProxyHistoryHandler(self)
        
        