def selectionSort(arr):
    for i in range(len(arr)):
        min_= i
        for j in range(i+1, len(arr)):
            if arr[min_] > arr[j]:
                min_ = j
    #swap
        arr[i], arr[min_] = arr[min_], arr[i]


# create a list 
arr = list(map(int,input("Enter numbers to create a list: ").strip().split())) 

selectionSort(arr)

print("The sorted list is ")
for i in range(len(arr)):
    print(arr[i],end=" ")