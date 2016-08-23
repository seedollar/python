class Person:
    # Like a constructor with a single argument
    def __init__(self, name):
        self.name = name

john = Person("John")
print(john.name)

