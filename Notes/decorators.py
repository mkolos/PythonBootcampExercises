def hello(name='Jose'):
    return 'Hello ' + name


hello()
# print 'Hello Jose'

greet = hello
greet
# print <function __main__.hello>

greet()


# print Hello Jose

def hello(name='Jose'):
    print('The hello() function has been executed')

    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return "\t This is inside the welcome() function"

    print(greet())
    print(welcome())
    print("Now we are back inside the hello() function")


hello()


# print
# The hello() function has been executed
# 	 This is inside the greet() function
# 	 This is inside the welcome() function
# Now we are back inside the hello() function


def new_decorator(func):
    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func


def func_needs_decorator():
    print("This function is in need of a Decorator")


func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()


# Code would be here, before executing the func
# This function is in need of a Decorator
# Code here will execute after the func()

@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator")


func_needs_decorator()
# Code would be here, before executing the func
# This function is in need of a Decorator
# Code here will execute after the func()
