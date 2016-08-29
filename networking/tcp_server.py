# Example of how to send data over TCP protocol. Used in conjunction with the tcp_server.py file.
from datetime import datetime
import socket

address = ('localhost', 6789)
max_size = 1000

print("Starting the server at", datetime.now())
print("Waiting for a client to call...")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(5)

client, addr = server.accept()
data = client.recv(max_size)

print("At",datetime.now(),client,"said",data)
client.send(b"Are you talking to me?")
client.close()
server.close()
