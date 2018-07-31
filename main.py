import sys
import asyncio
from game_server import GameServer

from servers import select_server

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    try:
        # maps = MapServer(loop).start('maps.poke.one', 2015)

        game = GameServer(loop).start(select_server("game"), 2012)

        # loop.create_task(maps)
        loop.run_until_complete(game)
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    except Exception as exc:
        print(exc, file=sys.stderr)
    finally:
        loop.close()