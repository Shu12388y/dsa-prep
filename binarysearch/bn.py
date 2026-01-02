# Binary Search
arr = [0,0,0,0,0,1,1,1,1]

def binarySearch(arr:list)->int:
    left,right = 0, len(arr) -1 
    while (left + 1< right):
        M = (left + right) // 2
        if arr[M] == 0:
            left = M 
        else:
            right = M 
    return right
print(binarySearch(arr))