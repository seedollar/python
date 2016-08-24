# Example of how to use the "namedtuple" function from the standard library
from collections import namedtuple

# Define a namedtuple where the first parameter is the type name (MuscleCar), and the second param is the list of attributes
MuscleCar = namedtuple('MuscleCar', 'color engine dubs')
audis7 = MuscleCar('red', 'V8', '21 inch')

print(audis7.color)
print(audis7.engine)
print(audis7[2])


