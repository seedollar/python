import socket

print(socket.gethostbyname("www.explosm.net"))
print(socket.gethostbyname_ex("www.explosm.net"))
print(socket.getaddrinfo("www.explosm.net", 80))

print(socket.getservbyname("ftp"))
print(socket.getservbyport(22))
