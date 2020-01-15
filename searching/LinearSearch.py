
# function to do linear search
def LinearSearch(list,item):
    for i in range(0,len(list)):
        if list[i] == item:
            return i
        else:
            return -1

# create a list 
inputList = list(map(int,input("Enter numbers to create a list: ").strip().split())) 

# Search
item = int(input("Enter item to search: "))
LinearSearch(inputList,item)

# display result
while(True):
    if LinearSearch(inputList,item) == -1:
        print(f"{item} is not in the list")
    else:
        print(f"{item} is at position {LinearSearch(inputList,item)}")



