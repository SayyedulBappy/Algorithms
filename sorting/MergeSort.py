
def mergeSort(arr): 
	if len(arr) >1: 
		mid = len(arr)//2 #mid of the array 
		L = arr[:mid] # Dividing the array elements 
		R = arr[mid:] # into 2 halves 

		mergeSort(L) # Sorting the first half 
		mergeSort(R) # Sorting the second half 

		i = j = k = 0
		
		# Copy data to temp arrays L[] and R[] 
		while i < len(L) and j < len(R): 
			if L[i] < R[j]: 
				arr[k] = L[i] 
				i+=1
			else: 
				arr[k] = R[j] 
				j+=1
			k+=1
		
		# Checking if any element was left 
		while i < len(L): 
			arr[k] = L[i] 
			i+=1
			k+=1
		
		while j < len(R): 
			arr[k] = R[j] 
			j+=1
			k+=1

def printList(arr): 
	for i in range(len(arr)):		 
		print(arr[i],end=" ") 
	print() 


if __name__ == '__main__': 
	arr = list(map(int,input("Enter numbers to create a list: ").strip().split()))
	print ("Given array is: ") 
	printList(arr) 
	mergeSort(arr) 
	print("Sorted array is: ") 
	printList(arr) 
