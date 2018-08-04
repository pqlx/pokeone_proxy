from typing import *
import sys
from UI.widgets import Ui_MainWindow
from UI.Startup import Startup
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QHeaderView
from PyQt5.QtCore import pyqtSignal, pyqtSlot
import json

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
                            self.packets[x], 
                            indent=4, 
                            separators=(',', ': ')
                        )
        )
        
        