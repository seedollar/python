# This example shows how to read in a text file in a chunked way

fin = open("relativity", "rt")
chunk = 100
poem = ''

while True:
    print("reading...")
    fragment = fin.read(chunk)
    if not fragment:
        break
    else:
        poem += fragment

fin.close()

print(poem)