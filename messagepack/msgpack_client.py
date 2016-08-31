from msgpackrpc import Client, Address

client = Client(Address("localhost", 6789))
num = 16
result = client.call('double', num)
print("Double %s is %s" % (num, result))