# Create your own exception class and "raise" it when required

class UnderAgeException(Exception):
    pass

while True:
    val = int(input("What is your age: "))
    if (val == 'q'):
        break

    if (val < 21):
        raise UnderAgeException('You are under age!!!')
    else:
        print("Welcome in!!")

