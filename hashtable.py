# https://github.com/calebmadrigal/algorithms-in-python/blob/master/hashtable.py

############ HashTable helper functions
def hash_val(key_str, hashtable_size):
	# ord() function: 
	# input: 1 character
	# return: unicode of the character. ex: 'a' has unicode of 97
    return sum([ord(c) for c in key_str]) % hashtable_size

key = 'apple'
print(hash_val(key, 15))
