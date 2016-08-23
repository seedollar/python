# Illustrates the use of the collections "Counter" module which aggregates dictionary keys

from collections import Counter

food = ['eggs','bacon', 'toast','sausage', 'beans', 'bacon', 'eggs']
breakfast =['eggs', 'toast']

food_counter = Counter(food)
breakfast_counter = Counter(breakfast)

print(food_counter.most_common(1))

print("Food:", food_counter)
print("Breakfast:",breakfast_counter)

diet = food_counter + breakfast_counter # We can add the 2 counters together using the "+" sign

common_foods = food_counter & breakfast_counter # You can also apply comparison operators on Counter variables
print("common foods:", common_foods)

union_foods = food_counter | breakfast_counter # You can also apply comparison operators on Counter variables
print("union foods:", union_foods)

print("Diet:", diet)