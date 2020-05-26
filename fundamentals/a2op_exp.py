a = 2
a *= 3

print(a)
# = 6
print(True or False)

length = 5
width = 2

area = length * width
print('Area' + ' is', area)
# concatenation can only be done with strings.
# the comma denotes variables that should be compiled to text and then concatenated with a space between
print('Perimeter is', 2 * (length + width))
# Python also "pretty-prints", so it automatically adds spaces before variables when added to a string

# to make a custom separator:
print('cats', 'dogs', 'mice', sep=',')
# output: "cats,dogs,mice"
