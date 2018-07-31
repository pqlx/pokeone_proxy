from typing import *

import random

servers = {
    "game_servers": [

        {
            "ip": "95.183.48.120",
            "dns_entry": "game.poke.one"
        },
        {
            "ip": "95.183.48.68",
            "dns_entry": "game2.poke.one"
        },
        {
            "ip": "95.183.48.225",
            "dns_entry": "game3.poke.one"
        },
        {
            "ip": "95.183.48.16",
            "dns_entry": "game4.poke.one"
        }

    ],
    "map_servers": [
        {
            "ip": "95.183.55.67",
            "dns_entry": "maps.poke.one"
        }

    ]
}

def select_server(server_type: str) -> str:
    if server_type == "maps":
        operand = servers["map_servers"]
    else:
        operand = servers["game_servers"]
    
    return random.choice(operand)["ip"]
