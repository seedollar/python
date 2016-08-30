# Example of how to perform XML RPC. Used on conjunction with the xmlrpc_server.py file
import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:6789/")
num = 19

result = proxy.double(num)
print("Double %s is %s" % (num, result))
