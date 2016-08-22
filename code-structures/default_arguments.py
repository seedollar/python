# Default arguement values can be set, and will be used in cases where the argument is not specified
def capture_dog(breed, color, destroy=False):
    print("The dog breed is", breed, "with colour", color, "and should be destroyed =", destroy)

capture_dog("Maltese", "white", True)
capture_dog("Poodle", "brown")
