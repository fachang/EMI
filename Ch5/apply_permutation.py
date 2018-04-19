#!/user/bin/python

A = [10, 2, 3, 4]
P = [1, 3, 2, 0]

def apply_permutation_brute_force(perm, A):
	B = [0]*len(A)
	for i in xrange(len(A)):
		B[P[i]] = A[i]
	return B

'''
Space O(1)
Time  O(n)
Key: When this element is processed, mark this place
'''
def apply_permutation_opt1(perm, A):
	for i in xrange(len(A)):
		next = i
		while P[next] >= 0:
			A[next], A[P[next]] = A[P[next]], A[next]
			next = P[next]
			P[next] -= len(A)

	return A


def apply_permutation_opt2(perm, A):
	
	def cyclic_permutation(start, perm, A):
		i, temp = start, A[start]
		while True:
			next_i = perm[i]
			next_temp = A[next_i]
			A[next_i] = temp
			i, temp = next_i, next_temp
			if i == start:
				break

	for i in xrange(len(A)):

		j = perm[i]
		while i != j:
			if j < i:
				break
			j = perm[j]
		else:
			cyclic_permutation(i, perm, A)

	return A

if __name__ == '__main__':
	print 'Brute force',apply_permutation_brute_force(P, A)
	#print apply_permutation_opt1(P, A)
	print apply_permutation_opt2(P, A)