
# Passing tuples around

# Ever wished you could return two different values from a function?
# You can. All you have to do is use a tuple.

def get_error_details():
    return (2, 'details')


errnum, errstr = get_error_details()

print(errnum)
print(errstr)


print()
print()


# Notice that the usage of a, b = <some expression> interprets
# the result of the expression as a tuple with two values.
# This also means the fastest way to swap two variables in Python is:

a = 5
b = 8

print(a, b)

print('flipping them')
a, b = b, a

print(a, b)


# Special Methods
# http://docs.python.org/3/reference/datamodel.html#special-method-names

# __init__(self, ...)
    # This method is called just before the newly created object is returned for usage.
# __del__(self)
    # Called just before the object is destroyed (which has unpredictable timing, so avoid using this)
# __str__(self)
    # Called when we use the print function or when str() is used.
# __lt__(self, other)
    # Called when the less than operator (<) is used. Similarly, there are special methods for all the operators (+, >, etc.)
# __getitem__(self, key)
    # Called when x[key] indexing operation is used.
# __len__(self)
    # Called when the built-in len() function is used for the sequence object.


print()
print()


# Lambda forms:

# A lambda statement is used to create new function objects. Essentially, the lambda takes a parameter followed by a single expression. Lambda becomes the body of the function. The value of this expression is returned by the new function.

points = [{'x': 2, 'y': 3},
          {'x': 4, 'y': 1}]
points.sort(key=lambda i: i['y'])
print(points)


# Output
# $ python more_lambda.py
# [{'x': 4, 'y': 1}, {'x': 2, 'y': 3}]


# List comprehension

listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2]

# Output: [6, 8]


print()
print()

# Receiving Tuples and Dictionaries in Functions


# There is a special way of receiving parameters to a
# function as a tuple or a dictionary using the * or ** prefix respectively.
# This is useful when taking variable number of arguments in the function.


def powersum(power, *args):
    '''Return the sum of each argument raised to the specified power.'''

    total = 0
    for i in args:
        total += pow(i, power)
    return total


print(powersum(2, 3, 4))
# Output: 25

print(powersum(2, 10))
# Output: 100

# Because we have a * prefix on the args variable,
# all extra arguments passed to the function are stored in args as a tuple.
# If a ** prefix had been used instead,
# the extra parameters would be considered to be key/value pairs of a dictionary.


# Assert statement:

mylist = ['item']
assert len(mylist) >= 1
mylist.pop()

# assert len(mylist) >= 1
# AssertionError


print()
print()


# Decorators
# Decorators are a shortcut to applying wrapper functions.
# This is helpful to "wrap" functionality
# with the same code over and over again.
# For example, I created a retry decorator for myself that
# I can just apply to any function and if any exception
# is thrown during a run, it is retried again,
# till a maximum of 5 times and with a delay between each retry.
# This is especially useful for situations where
# you are trying to make a network call to a remote computer:
#
# from time import sleep
# from functools import wraps
# import logging
# logging.basicConfig()
# log = logging.getLogger("retry")
#
#
# def retry(f):
#     @wraps(f)
#     def wrapper_function(*args, **kwargs):
#         MAX_ATTEMPTS = 5
#         for attempt in range(1, MAX_ATTEMPTS + 1):
#             try:
#                 return f(*args, **kwargs)
#             except Exception:
#                 log.exception("Attempt %s/%s failed : %s",
#                               attempt,
#                               MAX_ATTEMPTS,
#                               (args, kwargs))
#                 sleep(10 * attempt)
#         log.critical("All %s attempts failed : %s",
#                      MAX_ATTEMPTS,
#                      (args, kwargs))
#     return wrapper_function
#
#
# counter = 0
#
#
# @retry
# def save_to_database(arg):
#     print("Write to a database or make a network call or etc.")
#     print("This will be automatically retried if exception is thrown.")
#     global counter
#     counter += 1
#     # This will throw an exception in the first call
#     # And will work fine in the second call (i.e. a retry)
#     if counter < 2:
#         raise ValueError(arg)
#
#
# if __name__ == '__main__':
#     save_to_database("Some bad value")
# Output:
#
# $ python more_decorator.py
# Write to a database or make a network call or etc.
# This will be automatically retried if exception is thrown.
# ERROR:retry:Attempt 1/5 failed : (('Some bad value',), {})
# Traceback (most recent call last):
#   File "more_decorator.py", line 14, in wrapper_function
#     return f(*args, **kwargs)
#   File "more_decorator.py", line 39, in save_to_database
#     raise ValueError(arg)
# ValueError: Some bad value
# Write to a database or make a network call or etc.
# This will be automatically retried if exception is thrown.


