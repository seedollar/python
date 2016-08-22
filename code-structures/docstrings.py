# Illustration of how to document a function using a docstring.
def summation(*args):
    'This function takes in a tuple of parameters and aggregates the values and returns the sum'
    total = 0.0
    for num in args:
        total += num

    return total

help(summation)

print(summation(974,6, 10, 5, 5))
