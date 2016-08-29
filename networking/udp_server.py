# Illustrates how you can send an UDP message from a client and get the server to respond. Used on conjunction with
# the udp_client.py file.
from datetime import datetime
import socket

server_address = ('localhost', 6789)
max_size = 4096

print("Starting the server at", datetime.now())
print("Waitling for client to call...")
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(server_address)

data, client = server.recvfrom(max_size)

print("At", datetime.now(), client, "said", data)
server.sendto(b"Are you talking to me?", client)
server.close()


