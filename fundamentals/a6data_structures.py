
# There are four built-in data structures in Python
# - list, tuple, dictionary and set.

# List: ordered array of itmes, which can themselves store values of different types

list1 = [1, 2, 'sdf', 5]

list1.remove(1)
print(list1)
# output:
# [2, 'sdf', 5]
list1.append('something')
print(list1)
# output:
# [2, 'sdf', 5, 'something']

# Lists can also contain other list values
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam[1][4])
# output: 50


# List Concatenation and List Replication
# >>> [1, 2, 3] + ['A', 'B', 'C']
# [1, 2, 3, 'A', 'B', 'C']
# >>> ['X', 'Y', 'Z'] * 3
# ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
# >>> spam = [1, 2, 3]
# >>> spam = spam + ['A', 'B', 'C']
# >>> spam
# [1, 2, 3, 'A', 'B', 'C']


# When we use a variable i and assign a value to it,
# say integer 5 to it, you can think of it as creating an object
# (i.e. instance) i of class (i.e. type) int. In fact,
# you can read help(int) to understand this better.


def print_shoplist(items):
    for item in items:
        print(item, end=' ')


shoplist = ['apple', 'mango', 'carrot', 'banana']
print('\nI have', len(shoplist), 'items to purchase.')

# len() gets the number of values (length) that are in a list value passed into it

# end=' ' allows you to to not end the line with a \n
print('These items are:', end=' ')
print_shoplist(shoplist)
print()

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0] # remove that item from the list
print('I bought the', olditem)
print('My shopping list is now', end=' ')
print_shoplist(shoplist)

# You can grab subsections of lists, tuples, and strings, like so:
print('\n\nItem 1 to 3 is', shoplist[1:3])
print('Items 1 to -1 is', shoplist[1:-1]) # -1 refers to the last index in a list
print('Items start to end is', shoplist[:])
print('Items start to end, skipped every other', shoplist[::2])


# >>> 'howdy' in ['hello', 'hi', 'howdy', 'heyas']
# True
# >>> spam = ['hello', 'hi', 'howdy', 'heyas']
# >>> 'howdy' not in spam
# False

# Multiple assignment from a list:
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
# (The number of variables and the length of the list must be exactly equal, or ValueError)

# swap the values in two variables:
a, b = 'Alice', 'Bob'
a, b = b, a
print(a)
'Bob'


# Comma Code
def listConcat(list):
	listString = ''
	
	for i in range(len(list)):
		if (i == len(list)-1):
			listString += 'and ' + list[i]
		else:
			listString += list[i] + ', '
	
	return listString
		
		
listConcatExample = ['apples', 'bananas', 'tofu', 'cats']
listStrings = listConcat(listConcatExample)
print(listStrings)


# Strings and tuples act similarly to lists
# >>> name = 'Zophie'
# >>> name[0]
# 'Z'

# A list value is a mutable data type: It can have values added, removed, or changed. 
# However, a string or tuple is immutable: It cannot be changed. 


# Tuples:
# They hold together multiple objects, but have less functionality
# than lists. Immutable, so you can't modify them.

zoo = ('python', 'elephant', 'penguin')
print('\nNumber of animals in the zoo is', len(zoo))

new_zoo = 'monkey', 'camel', zoo
# parentheses not required but are a good idea
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is',
      len(new_zoo)-1+len(new_zoo[2]))

# Result
# Number of cages in the new zoo is 3
# All animals in new zoo are ('monkey', 'camel', ('python', 'elephant', 'penguin'))
# Animals brought from old zoo are ('python', 'elephant', 'penguin')
# Last animal brought from old zoo is penguin
# Number of animals in the new zoo is 5

# If you want to make an empty tuple:
myempty = ()
# If you want a tuple with only one object (aka a singleton):
myempty = (2,)


# Dictionary (dict class):
ab = {
    'RJ': 'r@j.com',
    'Grant': 'g@g.org',
    'Brandon': 'b@avery.com',
    'Tara': 'tara@arat.com'
}

print("Grant's address is", ab['Grant'])

# Deleting a key-value pair
del ab['Brandon']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

# Adding a key-value pair
ab['Claire'] = 'claire@avery.org'

if 'Claire' in ab:
    print("\nClaire's address is", ab['Claire'])


# Set: an unordered collection of simple objects
myset = set(['brazil', 'russia', 'india'])
if 'india' in myset:
    print('\nfound')
else:
    print('\nnot found')

myset2 = myset.copy()
myset2.add('china')
print(myset2.issuperset(myset))
# True
myset.remove('russia')
print(myset & myset2)
# OR myset.intersection(myset2)
# result: {'brazil', 'india'}


# References:
shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist is just another name (variable) pointing to the same object,
# so later they will both be "updated" by just deleting from one
# this is only an issue for complex objects like lists,
# not simple objects like ints
mylist = shoplist

del shoplist[0]
print('\nshoplist is', shoplist)
print('mylist is', mylist)

# Make a copy by doing a full slice
mylist = shoplist[:]

del mylist[0]
print('\nshoplist is', shoplist)
print('mylist is', mylist)


# copy.copy() creates a second item that can be modified independently of the first but contains the same info
# >>> import copy
# >>> spam = ['A', 'B', 'C', 'D']
# >>> cheese = copy.copy(spam)
# >>> cheese[1] = 42
# >>> spam
# ['A', 'B', 'C', 'D']
# >>> cheese
# ['A', 42, 'C', 'D']

# The deepcopy() function will copy these inner lists as well.


# More with strings:
delimiter = ', '
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))


