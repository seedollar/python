#Generator functions allow for the sequence creation of objects. The keyword used is "yield"

def my_sequence(start=50, end=0, step=2):
    number = start / 2
    while number > 0:
        yield int(number)
        number -= step

for counter in my_sequence():
    print(counter)

print(type(my_sequence))
