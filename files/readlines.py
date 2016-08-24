# Illustration of using the readlines function that will read text line by line, then return a list of one-line strings

fin = open("relativity", 'rt')

lines = fin.readlines()

fin.close()

for line in lines:
    print(line)

