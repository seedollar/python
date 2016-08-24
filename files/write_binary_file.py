# Shows the use of the 'b' file flag to write bytes to the file

# generate mock bytes

bdata = bytes(range(0, 256))
print(len(bdata))

fout = open('binaryfile', 'wb')

fout.write(bdata)

fout.close()
