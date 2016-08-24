# Give an example of a "static method" which is a convienience method that can be called by either a instance or the class itself

class Nuke():
    @staticmethod
    def brand():
        print("Mother Russia")

# Notice you can just call the method directly
Nuke.brand()

bomb1 = Nuke()
bomb1.brand()

