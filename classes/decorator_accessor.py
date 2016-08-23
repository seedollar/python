class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

c = Circle(5)
print(c.diameter)
c.radius = 8
print(c.diameter)

# Can't do the below as it will fail.
# c.diameter = 10
