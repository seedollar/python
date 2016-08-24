# You can also use the print() function to write text to a file. The print() appends a new line at the end.

poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''

fout = open("relativity2", "wt")
print(poem, file=fout, sep='', end='')
fout.close()

