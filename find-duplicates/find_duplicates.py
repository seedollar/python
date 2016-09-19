fin = open("numbers_new.txt", "rt")

numbers = fin.readlines()

fin.close()

unique_list = []

# Let's iterate through all the numbers and root out any duplicates.
for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

print("Numbers Size: ", len(numbers))
print("Unique List Size: ", len(unique_list))

if len(numbers) == len(unique_list):
    print("Numbers are unique")
else:
    print("Numbers have duplicates")



