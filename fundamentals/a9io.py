# 5/30/19


def reverse(text):
    # Flip items end to start, going back 1 at a time
    return text[::-1]


def is_palindrome(text):
    print(text)
    alphanum = ''.join(e for e in text if e.isalnum())
    print(alphanum)

    return alphanum == reverse(alphanum)


something = input('Enter text: ')
if is_palindrome(something):
    print('Palindrome')
else:
    print('No palindrome')


print()
print()

poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
use Python!
'''


def printlines(text):
    while True:
        line = text.readline()
        if len(line) == 0:
            break

        print(line, end='')


# Open for 'w'riting
f = open('poem.txt', 'w')
# Write text to file
f.write(poem)
# Close the file
f.close()


# If no mode is specified, 'r'ead mode is assumed by default
f = open('poem.txt')

printlines(f)
f.close()


# 'a' would append to the file
# you can also choose text 't' or binary 'b' modes
# Example to read the binary:
# g = open('poem.txt', 'rb')


print()
print()


# Python provides a standard module called pickle which you can use
# to store any plain Python object in a file and then get it back later.
# This is called storing the object persistently.
import pickle

shoplistfile = 'shoplist.data'
shoplist = ['apple', 'mango', 'carrot']

f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
f.close()

del shoplist

f = open(shoplistfile, 'rb')

storedlist = pickle.load(f)
print(storedlist)
f.close()



