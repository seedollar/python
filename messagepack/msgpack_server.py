# Example of how to use the MessagePack RPC library. Used on conjunction with the msgpack_client.py file.

from msgpackrpc import Server, Address

class Services():
    def double(self, num):
        return num * 2

server = Server(Services())
server.listen(Address("localhost", 6789))
server.start()