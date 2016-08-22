# A function can be defined within another function

def outer(name, age):
    def inner(param1, param2):
        return "Name:", param1, "Age:", param2

    return inner(name, age)

print(outer("Henry", 88))
