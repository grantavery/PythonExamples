
# There are four built-in data structures in Python
# - list, tuple, dictionary and set.

list1 = [1, 2, 'sdf', 5]

list1.remove(1)
print(list1)
# result:
# [2, 'sdf', 5]
list1.append('something')
print(list1)
# result:
# [2, 'sdf', 5, 'something']


# When we use a variable i and assign a value to it,
# say integer 5 to it, you can think of it as creating an object
# (i.e. instance) i of class (i.e. type) int. In fact,
# you can read help(int) to understand this better.


def print_shoplist(items):
    for item in items:
        print(item, end=' ')


shoplist = ['apple', 'mango', 'carrot', 'banana']
print('\nI have', len(shoplist), 'items to purchase.')

# end=' ' allows you to to not end the line with a \n
print('These items are:', end=' ')
print_shoplist(shoplist)
print()

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', end=' ')
print_shoplist(shoplist)

# You can grab subsections of lists, tuples, and strings, like so:
print('\n\nItem 1 to 3 is', shoplist[1:3])
print('Items 1 to -1 is', shoplist[1:-1])
print('Items start to end is', shoplist[:])
print('Items start to end, skipped every other', shoplist[::2])


# Tuples:
# They hold together multiple objects, but have less functionality
# than lists. Immutable, so you can't modify them

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
# mylist is just another name pointing to the same object,
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


# More with strings:
delimiter = ', '
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))