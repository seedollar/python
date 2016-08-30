# Example of how to perform XMLRPC. This file is used on conjunction with the xmlrpc_client.py
from xmlrpc.server import SimpleXMLRPCServer

def double(value):
    return value * 2

server = SimpleXMLRPCServer(('localhost', 6789))
server.register_function(double, "double")
server.serve_forever()
