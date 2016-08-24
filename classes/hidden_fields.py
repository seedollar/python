# Demonstrate how Python uses hidden fields by appending prefix of "__" to variable names
class Duck():
    def __init__(self, name):
        self.__hidden_name = name

    @property
    def name(self):
        return self.__hidden_name

    @name.setter
    def name(self, name):
        self.__hidden_name = name

donald = Duck("Donald")

print(donald.name)

donald.name = "Daffy"

print(donald.name)

# This statement will fail because the __ prefix makes sure the __hidden_name field is not easily found, but is still actually accessible
# print(donald.__hidden_name)

# Although the __hidden_name is more difficult to find, it's still accessible with this name
print(donald._Duck__hidden_name)

