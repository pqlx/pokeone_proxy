
from proxy import ProxyServer
from parser import packet_decode

class GameServer(ProxyServer):

    async def handle_send(self, packet: bytes):
        """ Intercept client -> proxy """
        # data = packet_decode(data, 'game', False)
        # ... do stuff with data
        # ... convert data back into bytes
        
        decoded = packet_decode(packet, 'game', False)
        print(decoded)

        return packet

    async def handle_recv(self, packet: bytes):
        """ Intercept proxy -> client """
        # data = packet_decode(data, 'game', True)
        # ... do stuff with data
        # ... convert data back into bytes

        return packet