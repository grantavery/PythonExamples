# Methods
# methods modify variables in-place, 
# meaning you don't need to do any assignment to capture the "new" value

# .index()
spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('heyas')
# output: 3
# (When there are duplicates of the value in the list, the index of its first appearance is returned.)

# .append() adds value to end of list
spam.append("yo")
print(spam)

# .insert() adds value at the index supplied, moving everything after it down a spot in the line
spam.insert(1, "hey")
print(spam)
# output: ['hello', 'hey', 'hi', 'howdy', 'heyas', 'yo']


# While The del statement will delete values at an index in a list, 
# '.remove()' is supplied a value and removes it from the list
spam.remove('hi') # removes 'hi'
del spam[4] # removes 'yo'
print(spam)
# output: ['hello', 'hey', 'howdy', 'heyas']

# .sort() 
spam.sort()
print(spam)
# output ['hello', 'hey', 'heyas', 'howdy']

# .sort(reverse=True) does the same in reverse

# sort() uses “ASCIIbetical order” rather than actual alphabetical order for sorting strings. This means uppercase letters come before lowercase letters.

spam2 = ['a', 'z', 'A', 'Z']
spam2.sort(key=str.lower)
print(spam2)
# ['a', 'A', 'z', 'Z']