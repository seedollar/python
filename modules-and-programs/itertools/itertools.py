# Examples of how to use the itertools class
import itertools

# the "chain()" method will merge the lists into one
for item in itertools.chain(['a', 'b'], [1,2,3]):
    print(item)

# accumulate will aggregate each element
for val in itertools.accumulate([10, 20, 30]):
    print(val)

# accumulate will aggregate each element and apply the lambda function
for val in itertools.accumulate([5, 10, 15], lambda e1, e2: e1 * e2):
    print(val)