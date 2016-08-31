# Example of how to use timers to measure performance of code
from time import time

t1 = time() # Capture a time now

num = 5
num *= 2

# Measure the difference in time from now to get the balance
print(time() - t1)