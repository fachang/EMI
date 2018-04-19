#!/user/bin/python
#>> << | & ~ ^ 
def add(a, b):

	carryIn = 0
	s = 0
	running_sum = 0
	k = 1
	tempA, tempB = a, b
	while tempA or tempB:
		Ak, Bk = a & k, b & k
		s = Ak ^ Bk ^ carryIn
		carryOut = (Ak & Bk) | (Ak & carryIn) | (Bk & carryIn)
		tempA, tempB = tempA >> 1, tempB >> 1
		running_sum |= s
		carryIn = carryOut << 1
		k = k << 1
	return running_sum | carryIn
		
		
	

def multiply(a, b):

	running_sum = 0
	# AxB ----> multiple A and its shift value
	while b: 
		if b & 1:
			running_sum = add(running_sum, a)
		a = a << 1
		b = b >> 1

	return running_sum
	


if __name__ == '__main__':
	print multiply(31, 10)