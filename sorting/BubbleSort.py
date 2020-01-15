
def bubbleSort(arr):
	n = len(arr)

	# Traverse through all array elements
	for i in range(n):

		# Last i elements are already in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]


# create a list 
arr = list(map(int,input("Enter numbers to create a list: ").strip().split())) 


bubbleSort(arr)

print ("Sorted list is:")
for i in range(len(arr)):
	print(arr[i],end=" ") 
