def sortStringArray(lex, alist, n): 
	a = sorted(alist, key = lambda word: [lex.index(c) for c in word]) #sorting by defining key of lex order
        
	for i in alist: 
		print(i) 
lex = "rcta"                   #new lex order in which the list will be sorted
alist = ['car','rat','cat']    #list to be sorted
n = len(alist) 
sortStringArray(lex, alist, n) #passing the parameters

