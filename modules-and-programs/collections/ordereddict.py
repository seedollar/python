# Illustrate the use of the OrderedDict from the collections standard library
from collections import OrderedDict

# will be captured in the same order when you print it out
ordered_items = OrderedDict([('Book', 'reading'), ('Car', 'driving'),('Piano', 'playing')])

for key in ordered_items:
    print(key)
