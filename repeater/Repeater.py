from typing import *
from PyQt5.QtWidgets import QMainWindow
from packetparser import packet_encode
from proxy import ProxyServer, ProxyConnection
import base64

class Repeater(object):

    def __init__(window: QMainWindow, server: ProxyConnection):
        self.window = window
        self.server = server

    def send(self, checked: bool):
        contents = self.window.ui.repeater_edit

        
