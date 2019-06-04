def lastele(n):
	return n[-1]                      #find the last element
def sort (tuples):
	return sorted(tuples, key=lastele)#sort with key stated as based on last element
lt=input("enter the list of tuple: ")     #input of tuples in a list
print("the sorted list of tuple is :")    #output
print(sort(lt))
