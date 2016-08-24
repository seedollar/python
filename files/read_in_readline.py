fin = open("relativity", "rt")
poem = ''

while True:
    line = fin.readline()
    if not line:
        break
    else:
        print("line read: ", line)
        poem += line

fin.close()

print(poem)