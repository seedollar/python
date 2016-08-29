# Example of how to send data over TCP protocol. Used in conjunction with the tcp_server.py file.
import socket
from datetime import datetime

address = ('localhost', 6789)
max_size = 1000

print("Starting the client at", datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
client.sendall(b"Sup!")
data = client.recv(max_size)
print('At', datetime.now(),"someone replied", data)
client.close()
