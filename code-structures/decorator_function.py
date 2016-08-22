# Takes a function as a parameter and does some different processing on it without modifying the original function.
def decorator_print_args(func):
    def decorator(*args):
        for word in args:
            print(word)
        return func(*args)
    return decorator

def decorator_double_args(func):
    def double(*args):
        result = func(*args)
        result = result * result
        print(result)
        return result
    return double

def normalMethod(a,b,c):
    print(a,b,c)

# the decorator is defined here
executeMethod = decorator_print_args(normalMethod)

executeMethod("test1","test2","test3")

# You can also use the annotations to apply the decorator function. The decorator that's closest to the def keyword is applied first.
@decorator_print_args
@decorator_double_args
def normalMethod2(e, f):
    print(e, f)
    return 5

normalMethod2(1, 2)



