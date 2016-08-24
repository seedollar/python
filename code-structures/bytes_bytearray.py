# Examples of how to use the "bytes"  and "bytearray" functions
# A bytes variable is immutable, whereas a bytearray variable is mutable.

blist = [1,64,13,6,36]
the_bytes = bytes(blist)
print("Bytes: ", the_bytes)

the_byte_array = bytearray(blist)
print("Bytearray: ", the_byte_array)
