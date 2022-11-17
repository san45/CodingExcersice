```
Given a string and a number k, find the k’th non-repeating character in the string. 
Input : str = geeksforgeeks, k = 3
Output : r
First non-repeating character is f,
second is o and third is r.

Input : str = geeksforgeeks, k = 2
Output : o

Input : str = geeksforgeeks, k = 4
Output : -1

```

def find_first_rep(string,k):
	dict={}
	for each in string: 
		dict[each] = dict.get(each,0) + 1
	print(dict)
	count=0
	for each in string:
		print(each,dict[each])
		if dict[each] == 1:
			count +=1
			if count == k :
				return each
	return "-1"
				
	
print(find_first_rep("geeksforgeeks",2))

#TEST
