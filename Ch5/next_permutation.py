#!/user/bin/python

s = [4, 2, 5, 1, 3, 0]

def next_permutation(s):
	# (1) Find the point to separate descrease sequence and the other part
	# Ex. [6, 2, 1, 5, 4, 3, 0]
	#            ^
	sepPoint = 0
	for i in reversed(xrange(len(s))):
		if s[i - 1] < s[i]:
			print s[i-1]
			sepPoint = i - 1
			break
	# (2) Swap seqarate point and the number larger seqarate point at least
	#     in the decreased oredr sequence 
	for i in reversed(xrange(len(s))):
		if s[i] > s[sepPoint]:
			s[i], s[sepPoint] = s[sepPoint], s[i] 
			break
	# (3) Reverse sequence after separation point to get smaller dictionary order
	s[sepPoint + 1 : ] = reversed(s[sepPoint + 1 :])
	return s

if __name__ == '__main__':


	print next_permutation(s)
