# Binary Search

arr = [0,0,0,0,0,1,1,1,1]

# target = 0

# T.C. O(n)
# for i in range(len(arr)):
#     if arr[i] == 1:
#         target = i
#         break  
    
# print(target)


# T.C. O(log2N)
def binarySearch(a:list)->int:
    left,right = 0, len(a) - 1
    while left < right:
        base = (right + left) // 2
        if  a[base] == 1 and a[base  - 1] != 1:
            return base 
        elif a[base] < 1:
            left  = base
        elif a[base] >= 1:
            right = base
    else:
        return -1

print(binarySearch(arr))    