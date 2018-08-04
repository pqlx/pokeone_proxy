from typing import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QTimer

class Startup(QApplication):
    """
    QApplication wrapper to allow executing a callable after the GUI has started up.
    """
    started = pyqtSignal()

    def __init__(self, args):
        super().__init__(args)
        QTimer.singleShot(0, self.started.emit)

    def set_signal(self, handler: Callable):
        self.started.connect(handler)
