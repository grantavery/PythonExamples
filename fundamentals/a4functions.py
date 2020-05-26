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
def func1(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)


func1(x)
print('x is still', x)


# use the global statement to assign a value
# to a name defined at the global scope
x = 55


def func2():
    # this has to be in the inner scope:
    global x

    print('x is', x)
    x = 2
    print('Changed global x to', x)


func2()
print('Value of x is', x)

# Code in the global scope cannot use any local variables.
# However, a local scope can access global variables.
# Code in a function’s local scope cannot use variables in any other local scope.
# You can use the same name for different variables if they are in different scopes. That is, there can be a local variable named spam and a global variable also named spam.

# Why? memory constraints
# While using global variables in small programs is fine, it is a bad habit to rely on global variables as your programs get larger and larger.

# If you need to modify a global variable from within a function, use the global statement
def globalTest():
	global eggs
	eggs = 'local but global'

eggs = 'global'
globalTest()
print(eggs)
# output: 'local but global'

# Default values:
def say(message, times=1):
    return message * times


print(say('Hello'))
print(say('World', 5))
# Result (the multiplication is applied to the string variable:
# Hello
# WorldWorldWorldWorldWorld


# you can manually specify certain parameters but not others, like so:
def func3(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)


func3(3, 7)
func3(25, c=24)
func3(c=50, a=100)


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
def print_max2(a, b):
    """Prints the maximum of two numbers.

    The two values must be integers."""
    # convert to integers, if possible
    a = int(a)
    b = int(b)

    if a > b:
        print(a, 'is maximum')
    else:
        print(b, 'is maximum')


print_max2(3, 5)
print(print_max2.__doc__)

# Python treats everything as an object and this includes functions


# https://automatetheboringstuff.com/chapter3/

import random
def getAnswer(answerNumber):
	if answerNumber == 1:
		return 'It is certain'
	elif answerNumber == 2:
		return 'It is decidedly so'
	elif answerNumber == 3:
		return 'Yes'
	elif answerNumber == 4:
		return 'Reply hazy try again'
	elif answerNumber == 5:
		return 'Ask again later'
	elif answerNumber == 6:
		return 'Concentrate and ask again'
	elif answerNumber == 7:
		return 'My reply is no'
	elif answerNumber == 8:
		return 'Outlook not so good'
	elif answerNumber == 9:
		return 'Very doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

# Same as
print(getAnswer(random.randint(1, 9)))


# "None" is the equivalent of null/nil in other languages. Functions with no return value actually return None
# >>> spam = print('Hello!')
# Hello!
# >>> None == spam
# True
