def binarySearch(alist, l, r, ele): 
	while l <= r: 
		mid = l + (r - l)/2; 
		if alist[mid] == ele:                  # to check if the element is at the middle
			return mid 
		elif alist[mid] < ele:                 # if element is ahead of the middle index we leave the left part
			l = mid + 1
		else:                                  # If element is before the middle index we ignore right part
			r = mid - 1
	return -1      	                                #if element not found


alist = [4,2,1,3,5,6]
alist.sort()
ele = int(input("Enter the element to be searched : "))
result = binarySearch(alist, 0, len(alist)-1, ele)     # Calling the function
if result != -1: 
	print ("Element is present at index %d" % result) 
else:
	print("Element not found")
