"this is just a psuedo code"

'''
Stringbuilder: 
	In events when concatenating a list of string. Running time is often high.
	Why: 
		lets assume there are n strings of each length x. Upon each concatenation, a new string is concatenated
		and two strings are copied over. 
		First iteration requires : x characters copying.
		Second iteration requires: 2x characters copying and so on...

		Total time: O(x+2x+3x+.....nx) = O(xn^2)

	Stringbuilder helps solve this problem by creating a resizble array of all the strings. This way, 
	a new string copying is done only when necessary. 

	String joinwords(String[] words){
	Stringbuilder sentence = new Stringbuilder();
	for (String w: words){
		sentence.append(w);
	}
	return sentence.toString();
	}
'''

