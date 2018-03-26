'''URLify a string using Python. 
Replace all spaces with %20, 
so Mr John Smith becomes, Mr%20John%20Smith


1. Do this in place.
2. Determine complexity
3. You may assume that the string has sufficient space at the end to hold the additional characters 
and that you are given the true length of the string.
'''

text = 'Mr John Smith'#13 
special_str = '%20'
def URLify(text, text_len, special_str):
	url = [] 
	for i in range(text_len): # n
		if text[i] == ' ': # n-s
			url.append(special_str) # append() is O(1)
		else:
			url.append(text[i])

	print(url)
	return ''.join(url)


print(URLify(text, 13, '%20'))

'''
Notes: 
1. something like this won't work in python: 

if text[i] == ' ':
	text[i] = '%20'

this is because strings are immutable in python
'''