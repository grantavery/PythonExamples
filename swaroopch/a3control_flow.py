

# if/else; always evaluates True
if True:
    print('Yes, it is true')


# While, if/else, and try/except examples:
number = 23
running = True

while running:
    try:
        guess = int(input('Enter an integer: '))

        # If/else example:
        if guess == number:
            print('Correct')
            running = False
        elif guess < number:
            print('No, it was a bit higher')
        else:
            print('No, it was lower')
    except:
        print('Error! Please enter a valid integer.')
    else:
        print('(Nothing went wrong)')
    finally:
        print('(This gets run every time)')
else:
    print('While loop is done')
print('Done')


# for loop example:
for i in range(1, 5, 2):
    print(i)
else:
    print('For loop is done')
# If we supply a third number to range, then that becomes the step count.
# For example, range(1,5,2) gives [1,3]

# if you want the full list of numbers, call list() on the range()
# for example, list(range(5)) will result in [0, 1, 2, 3, 4]
print(list(range(1, 5)))


while True:
    s = input('Enter something : ')
    if s.lower() == 'quit':
        break
    print('Length of the string is', len(s))
print('Done')





