# Example of how to write some text is a chunked way
poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''

fout = open("chunked", "wt")
chunk = 100
offset = 0

while True:
    if (offset > len(poem)):
        break

    print("writing...")
    fout.write(poem[offset:offset+chunk])
    offset += chunk

fout.close()