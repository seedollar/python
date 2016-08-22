# This example will illustrate how you can pass a function and parameters to be executed by another function

def multiply(*args):
    total = 1
    for val in args:
        total *= val
    print("Multiplied:",total)

def invoke(func, *args):
    func(*args)


invoke(multiply, 9, 10)