# Illustrates how you reference another python file
import numtools # numtools here refers to the numtools.py file in the same directory as this file
from customcollections import orderedset # Shows how to reference a python dependency in a package named customcollections and referencing the file orderedset.py

print(numtools.int_to_str(9693))

s = orderedset.OrderedSet('abracadaba')
t = orderedset.OrderedSet('simsalabim')
print(s | t)
print(s & t)
print(s - t)



