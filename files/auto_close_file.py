# File streams can be automatically closed using the 'with' statement

with open('relativity', 'rt') as fout:
    contents = fout.read()

print(contents)
