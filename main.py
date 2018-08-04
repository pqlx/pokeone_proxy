import threading
import logging
import sys
import asyncio
import traceback
from game_server import GameServer
from servers import select_server
from UI.setup import MainUI

from PyQt5.QtWidgets import QTableWidget, QMainWindow


def thread_wrapper(function):

    def wrapper(*args, **kwargs):
        t = threading.Thread(target=function, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()
    
    return wrapper

@thread_wrapper
def start_server(window: QMainWindow):
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()

    try:
        
        game = GameServer(loop, window).start(select_server("game"), 2012)
        loop.run_until_complete(game)
        loop.run_forever()
    except Exception as exc:
        print(traceback.format_exc(), file=sys.stderr)
    finally:
        loop.close()


if __name__ == '__main__':

    m = MainUI()
    m.setup()
    m.run(start_server)
    
    
