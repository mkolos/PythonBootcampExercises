def myfunc(value):
    if value:
        return 'Hello'
    elif not value:
        return 'Goodbye'


def myfunc2(x, y, z):
    if z:
        return x
    elif not z:
        return y


def sum_of_numbers(a: int, b: int) -> int:
    return a + b


def is_even(value):
    if value % 2 == 0:
        return True
    else:
        return False


def is_greater(arg1, arg2):
    if arg1 > arg2:
        return True
    else:
        return False


def args(*args):
    return sum(args) * 0.05


def kwarg_example(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not fins any fruit here')


def arg_kwarg_example(*arg, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))


def arg_list_example(*args):
    even_numbers = []

    for item in args:
        if item % 2 == 0:
            even_numbers.append(item)

    return even_numbers


def transform_string(s):
    ret = ""
    i = True  # capitalize
    for char in s:
        if i:
            ret += char.upper()
        else:
            ret += char.lower()
        if char != ' ':
            i = not i
    return ret

