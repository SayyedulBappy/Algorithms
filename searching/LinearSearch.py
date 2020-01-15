
# function to do linear search
def LinearSearch(inputList,item):
    for i in range(0,len(inputList)):
        if inputList[i] == item:
            return i
    return -1
# create a list 
inputList = list(map(int,input("Enter numbers to create a list: ").strip().split())) 

# Search item
item = int(input("Enter item to search: "))

# display result
index = LinearSearch(inputList,item)
if index != -1: 
	print(f"{item} is at index {index}") 
else: 
	print(f"{item} is not in the list")



