# Example of writing some text to a file

poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''

fout = open('relativity', "wt")
fout.write(poem)
fout.close()

