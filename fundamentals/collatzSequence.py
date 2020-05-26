
def collatz(number):
	if (number % 2 == 0):
		# In python3, / operator does floating-point division while // does integer division (i.e. quotient without remainder))
		# whereas in Python 2, the / operator was simply integer division, unless one of the operands was already a floating point number.
		even = number // 2
		print (even)
		return even
	else:
		odd = (3 * number) + 1
		print (odd)
		return odd


print('Enter a number: ')

try:
	number = int(input())
except ValueError:
	print('Invalid input, please enter an integer')

while (number != 1):	
	number = collatz(number)

print(number)
