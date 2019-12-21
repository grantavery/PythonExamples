def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')


# for some reason it wants two lines both before and after function definitions
print_max(3, 4)
print_max(42, 42)

x = 5
y = 7

print_max(x, y)


# Local Variables:
# When you declare variables inside a function definition,
# they are not related in any way to other variables with the
# same names used outside the function -
# i.e. variable names are local to the function.
# This is called the scope of the variable.
# All variables have the scope of the block they are declared
# in starting from the point of definition of the name.
x = 50


# warning: "Shadows name 'x' from outer scope
def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)


func(x)
print('x is still', x)


# use the global statement to assign a value
# to a name defined at the global scope
x = 50


def func():
    # this has to be in the inner scope:
    global x

    print('x is', x)
    x = 2
    print('Changed global x to', x)


func()
print('Value of x is', x)


# Default values:
def say(message, times=1):
    return message * times


print(say('Hello'))
print(say('World', 5))
# Result (the multiplication is applied to the string variable:
# Hello
# WorldWorldWorldWorldWorld


# you can manually specify certain parameters but not others, like so:
def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)


func(3, 7)
func(25, c=24)
func(c=50, a=100)


# VarArgs (variable number of arguments) parameters
# I'm not sure how this works; how does it know
# which parameters are supposed to be 'numbers' objects,
# and which are 'phonebook' objects?
def total(a=5, *numbers, **phonebook):
    print('a', a)

    # iterate through all the items in tuple
    for single_item in numbers:
        print('single_item', single_item)

    # iterate through all the items in dictionary
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


total(10, 1, 2, 3, 1232, Jack="yo", John=2231, James=1560)


# documentation strings:
def print_max(a, b):
    """Prints the maximum of two numbers.

    The two values must be integers."""
    # convert to integers, if possible
    a = int(a)
    b = int(b)

    if a > b:
        print(a, 'is maximum')
    else:
        print(b, 'is maximum')


print_max(3, 5)
print(print_max.__doc__)

# Python treats everything as an object and this includes functions







