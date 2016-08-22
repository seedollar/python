# Generators only run once. They are not stored in memory

generator_seq = (number for num in range(1,10))
print(type(generator_seq))
print(generator_seq)
