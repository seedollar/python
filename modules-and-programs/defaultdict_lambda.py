# You can simply pass a lambda expression to the defaultdict function as well
from collections import defaultdict

# Use the lambda to return a default value of "Unknown" for missing key/value pair
items = defaultdict(lambda: "Unknown")

result = items['one']

print(result)

