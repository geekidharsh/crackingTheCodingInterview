# solution 1
def check_nth_bit_using_arr(i, n):
	# given and integer, check if it's nth bit is set or not. 
	# set and reset means: 
	# # 0 is not set 
	# 1 is set
	# Example: 
	# input: (integer, n) 
		# given 6, check if b0 is set or not.
		# so, bin of 6 is 110. now b0 here 
		# 1 1 0
		# b2 b1 b0
		# i.e b0 is 0
	# output: 
		# False

	# convert from int to bin
	bin = []
	# log N
	while i>0:
		i = i//2
		bin.append(i%2)


	if n<len(bin):
		if bin[len(bin)-1-n]&1:
			return 'set'
		else:
			return 'not set'
	else:
		return 'not enough bits'

		



# test: 
check_nth_bit(6,2)	



