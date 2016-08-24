# Use seek() to move to an offset in the file. Use tell() to tell you what the current offset is in the file

with open('relativity', 'rt') as fin:
    fin.seek(140)
    print(fin.tell())
    contents = fin.read()

print(contents)
