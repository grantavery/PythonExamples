

# https://python.swaroopch.com/basics.html
# and also some https://automatetheboringstuff.com

myNum = 100
if myNum > 50:
    print("High")
else:
    print("Low")
    print("yo")

print('''This is a multi-line string. This is the first line.
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
''')

age = 20
verb = "wrote"

print('{0} was {1} years old when he wrote this code.'.format(age, 'Grant'))

name = 'Grant'

print(f'{age} was {name} years old when he wrote this code.')

# decimal (.) precision of 3 to get it to return float '0.333'
print('{0:.3f}'.format(1/3))

# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('{0:_^11}'.format('hello'))

print('{name} wrote {code}'.format(name='Grant', code='python-examples'))

# print assumes new line \n , so to avoid that do this:
print('a', end='')
print('b', end=' ')
print('c', end='')
# output: "ab c"


print('What\'s your name?')

print('First line\nSecond line')

# "This is the first sentence. \
# This is the second sentence."
# is equivalent to
# "This is the first sentence. This is the second sentence."
# This is referred to as explicit line joining:
print("This is the first sentence. \
This is the second sentence.")

# literal/raw string:
# (Always use raw strings when dealing with regular expressions.)
print(r"Newlines are indicated by \n")


# Think of \ as saying, “This instruction continues on the next line.”
print('Four score and seven ' + \
      'years ago...')
			

# variable types can change:
age = 20
print(age)
age = 'twenty'
print(age)

# Python will always use indentation for blocks and will never use braces

