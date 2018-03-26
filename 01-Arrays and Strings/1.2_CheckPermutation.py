'''
Check Permutation: 
	Given two strings, write an algorithm to determine if one is Permutation of another. 
	determine O() and find best speed. 
Permutation: one of several possible variations, in which a set or number of things can be ordered or arranged.
P.S: string comparison is O(n), linear char by char. so the longer the char, the longer is the time
'''

# sample input 
a = 'sRF7w0qbGp4fdgEyNlscUFyouETaPHAiQ2WIxzohiafEGJLw03N8ALvqMw6reLN1kHRjDeDausQBEuIWkIBfqUtsaZcPGoqAIkLlugTxjxLhkRvq5d6i55l4oBH1QoaMXHIZC5nA0K5KPBD9uIwa789sP0ZKV4X6'
b = 'Vq3EeiLGfsAOH2PW6skMN8mEmUAtUKRDIY1kow9t1vIEhe81318wSMICGwf7Rv2qrLrpbeh8bh4hlRLZXDSMyZJYWfejLND4u9EhnNI51DXcQKrceKl9arWqOl7sWIw3EBkeu7Fw4TmyfYwPqCf6oUR0UIdsAVNw'
# solution 1: using sorting and join.
def checkPermutation(a,b):
	# input: strings a and b
	# return: boolean true if a is Permutation of b

	if len(a) != len(b): # O(1)
		return False
	else:
		s_a = ''.join(sorted(a)) # n + n
		s_b = ''.join(sorted(b)) # n + n
		if s_a == s_b: 
			return True
		else:
			return False


# solution 2: using hashing. Optimal solution
def is_permutation(a,b):
	if len(a) != len(b):
		return False
	
	count_a = {}
	count_b = {}
	for char in a:
		if char in count_a.keys():  # o(n) since looping through every char in string 
			count_a[char] += 1
		else: 
			count_a[char] = 1

	for char in b: # o(n) since looping through every char in string 
		if char in count_b.keys():
			count_b[char] += 1
		else:
			count_b[char] = 1

	for char in count_a:  # o(n) since looping through every char in string 
		if char not in count_b.keys():
			return False
		elif count_a[char] != count_b[char]:
			return False
	return True
		# total n + n + n = 3n or O(n)

is_permutation(a,b)
