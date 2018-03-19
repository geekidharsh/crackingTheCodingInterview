# Is Unique: Implement an algorithm to determine if a string has all the Unique characters, 
# what if you cannot use additional data structures

# using dynamic programming with hastable
def isUnique(inp_str, size):
	# Implement as hashtable, make every character in inp_str a key. 
	# keep multiple appearances of the char in hashtable[key] = array of indices
	hashtable = {} 
	i = 0
	for i in range(len(inp_str)):
		if inp_str[i] not in hashtable:
			hashtable[inp_str[i]] = [i]
		else:
			hashtable[inp_str[i]].append(i)
	print(hashtable)

# using only one data structure
def isUnique_alt(inp_str):
	uni = [] #storing unique char only
	for c in inp_str:
		if c not in uni:
			uni.append(c)
		else:
			print("duplicate character:", c)

inp_str = 'tigeress'
isUnique(inp_str, len(inp_str))
isUnique_alt(inp_str)
