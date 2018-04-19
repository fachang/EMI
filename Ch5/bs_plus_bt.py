#!/user/bin/python

def bt_plus_bs(a, b):

	a_list = list(a)
	b_list = list(b)

	if(len(a)>=len(b)):
		length = len(a)
		diff_length = len(a) - len(b)
		for idx in reversed(xrange(length)):
			if(idx-(diff_length)>=0):
				a_list[idx] = int(a_list[idx])+int(b_list[idx-diff_length])
		for idx in reversed(xrange(1, length)):
			if(int(a_list[idx])) >= 10:
				a_list[idx] = int(a_list[idx])-10
				a_list[idx-1] = int(a_list[idx-1]) + 1
		return ''.join(str(x)  for x in a_list)
	else:
		length = len(b)
		diff_length = len(b) - len(a)
		for idx in reversed(xrange(length)):
			if(idx-(diff_length)>=0):
				b_list[idx] = int(b_list[idx])+int(a_list[idx-diff_length])

		for idx in reversed(xrange(1, length)):
			if(int(b_list[idx])) >= 10:
				b_list[idx] = int(b_list[idx])-10
				b_list[idx-1] = int(b_list[idx-1]) + 1
		return ''.join(str(x)  for x in b_list)

			



if __name__ == '__main__':


	print bt_plus_bs("1999999", "456")
