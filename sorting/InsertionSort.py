
# Function to do insertion sort 
def insertionSort(arr): 
	# Traverse through 1 to len(arr) 
	for i in range(1, len(arr)): 
		key = arr[i] 
		# Move elements of arr[0..i-1], that are 
		# greater than key, to one position ahead 
		# of their current position 
		j = i-1
		while j >= 0 and key < arr[j] : 
				arr[j + 1] = arr[j] 
				j -= 1
		arr[j + 1] = key 

# create a list 
arr = list(map(int,input("Enter numbers to create a list: ").strip().split())) 

insertionSort(arr) 

print("Sorted list is: ")
for i in range(len(arr)): 
	print (arr[i],end=" ") 
