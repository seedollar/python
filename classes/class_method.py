# Give an example of how to define a class method that affects all instances of this class
class Employee():
    count = 0

    def __init__(self):
        Employee.count += 1
        self.shout()

    def shout(self):
        print("I have money!!!")

    @classmethod
    def employed(cls):
        print("%d have been employed" % cls.count)


empl1 = Employee()
empl2 = Employee()
empl3 = Employee()

Employee.employed()

