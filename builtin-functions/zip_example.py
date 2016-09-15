# An example of how to use the zip builtin python function. Zip will take 2 lists of equal size
# and pair their values together to form a key/value pair. If one list is less or greater than
# the other, the pairing algorithm terminates.

zip_result = zip('ABCD', '123')

print(type(zip_result))
print(zip_result)

for val in zip_result:
    print(val)
