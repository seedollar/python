# Illustrates how you can setup accessor methods on class fields. You can either use the "property()" function
# or decorator annotations to simulate the accessor invocations.

class Person():
    def __init__(self, name):
        self.hidden_name = name
        self.hidden_name2 = name

    def get_name(self):
        print("inside get_name()")
        return self.hidden_name

    def set_name(self, name):
        print("inside set_name()")
        self.hidden_name = name

    name = property(get_name, set_name)

    @property
    def name2(self):
        print("inside name2 GETTER")
        return self.hidden_name2

    @name2.setter
    def name2(self, name2):
        self.hidden_name2 = name2


robin = Person("Robin")

print(robin.name)

robin.name = "robin Hood"
print(robin.name)

santana = Person("Santana")
santana.name2 = "Carlos"
print(santana.name2)

