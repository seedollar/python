# Example of the flag 'x' which means you only write to the file if it doesn't already exist

poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''


try:
    fout = open("captivating", "xt")
    fout.write(poem)
    fout.close()
except FileExistsError:
    print("A file '{0}' already exists!".format("captivating"))

