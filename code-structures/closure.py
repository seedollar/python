# A function that is created dynamically and remember's the scope of variables it encounters

def shoutThis(phrase):
    def printPhrase():
        return "You shouted: '%s'" % phrase

    return printPhrase

isay = shoutThis("This is confusing!!!")

isay2 = shoutThis("My head is spinning!!!")

print(isay())
print(isay2())
