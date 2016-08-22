# Functions are first class citizens, and can therefore be assigned a variables and invoked.
# This example shows how functions can be passed as arguments and invoked.
def invoke(func):
    func()

def printMe():
    print("Printing...")

callMethod = printMe

invoke(callMethod)