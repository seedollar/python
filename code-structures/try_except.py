# An example of a try...except to catch exceptions and print something meaningful to the user

valid_numbers = [93,543,24,539,3861]
while True:
    val = input('Please enter a number between 0 and 4')
    if val == 'q':
        break

    try:
        value = valid_numbers[int(val)]
        print(value)
    except IndexError as ide:
        print("Invalid number. Must be between 0 and 4")
    except Exception as err:
        print("Bigger problems: Cause -", err)

