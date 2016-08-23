# Illustrates the use of the setdefault() method on a dictionary data type which ensures that if a key is missing, it's provided a default value
items = {'can': 1, 'cup': 2, 'fruit': 3}

item = items.setdefault('pen', 4)

print(item)

# If we setdefault on an existing key, the original value should be returned
item  = items.setdefault('can', 100)

print(item)