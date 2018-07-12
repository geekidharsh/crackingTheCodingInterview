# For instance, the binary representation of 6 is:
#     110

# The least significant bit is the bit on the far right
# of the binary representation and the most significant
# bit is the bit on the far left. We order the bits as

# b2, b1, b0
# 1   1   0


# 0 is not set 
# 1 is set


# 1 	0	 1
# b2  b1	b0


def int_to_bin(i):
	# convert from int to bin
	bin = []
	while i>0:
		i = i//2
		bin.append(i%2)
	bin = ''.join(str(i) for i in bin)
	return bin


