#!/user/bin/python

def divide(a, b):
	
	q = 0
	power = 32
	powerTmp = b << power
	while a >= b:
		while powerTmp > a:
			power -= 1
			powerTmp = powerTmp >> 1
		
		
		print "a", a, powerTmp, power
		a -= powerTmp
		
		q += 1<<power
	
	return q
if __name__ == '__main__':


	print divide(300, 3)