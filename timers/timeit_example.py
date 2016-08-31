# Example of how to use the timeit library
from timeit import timeit
from timeit import repeat

print(timeit('num = 5; num *= 2', number=1))

print(repeat('num = 5; num *= 2', number=1, repeat=5))
