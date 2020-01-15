
# Binary Search function
def binarySearch(arr, left, right, item): 

	while left <= right: 

		mid = int(left + (right - left)/2) 

		# Check if item is present at mid 
		if arr[mid] == item: 
			return mid 

		# If item is greater, ignore left half 
		elif arr[mid] < item: 
			left = mid + 1

		# If item is smaller, ignore right half 
		else: 
			right = mid - 1
	
	# If we reach here, then the element 
	# was not present 
	return -1

# create a list 
arr = list(map(str,input("Enter numbers to create a list: ").strip().split())) 

item = input("Enter item to search: ")

# Function call 
index = binarySearch(arr, 0, len(arr)-1, item)
if index != -1: 
	print(f"{item} is at index {index}") 
else: 
	print(f"{item} is not in the list")
