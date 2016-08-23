# Show how inheritance works in Python

class Car():
    def __init__(self):
        self.prefix = 'CAR'
    def get_wheel_count(self):
        return 4

    def get_color(self):
        return "You tell me"

    def get_prefix(self):
        return self.prefix

class Volkswagen(Car):
    def __init__(self):
        super().__init__() # We call the parent's __init__() method to initialize the prefix
        self.prefix += "-VW"
    def get_color(self):
        return "Green"

class Audi(Car):
    def __init__(self):
        super().__init__()
        self.prefix += "-AUDI"

golf = Volkswagen()
print(golf.get_wheel_count())
print(golf.get_color())
print(golf.get_prefix())

audiA6 = Audi()
print(audiA6.prefix)
