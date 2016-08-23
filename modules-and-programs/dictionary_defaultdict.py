# Illustrate the use of the defaultdict function from the collections standard library

from collections import defaultdict

items = defaultdict(int)

items['shirt'] = 84
items['bag'] # the default value will be a int 0

print(items)