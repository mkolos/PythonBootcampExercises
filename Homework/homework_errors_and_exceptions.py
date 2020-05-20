for i in ['a', 'b', 'c', 2]:
    try:
        print(i ** 2)
    except TypeError:
        print("Unsupported operand type(s) for ** or pow(): 'str' and 'int'")
    else:
        print("You passed the pow")

x = 5
y = 0

try:
    z = x / y
except ZeroDivisionError:
    print('Division by zero')
except:
    print('Failed')
else:
    print(z)


def ask():
    square = 0
    waiting = True
    while waiting:
        try:
            integer = int(input('Input an integer: '))
            square = integer ** 2
        except ValueError:
            print('An error occurred! Please try again!')
            continue
        else:
            waiting = False

    print('Thank you, your number squared is:  {}'.format(square))


ask()
