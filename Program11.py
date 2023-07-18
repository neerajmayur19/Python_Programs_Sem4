def binarysearch(lst,low,high,key):
    while(low <= high):
        mid = (low+high)//2
        if lst[mid] == key:
            return mid
        elif lst[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

lst = [1,2,3,4,5,6]
key = 6
index = binarysearch(lst,0,len(lst),key)
if index != -1:
    print(f"Element is found at the index {index}")
else:
    print("Element is not found at the index")
