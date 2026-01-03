# 

arr = [-2,3,4,5,5,5,5,6,7,8,9]



# def binarySearch(a:list,x:int):
#     left,right = 0 , len(a)
#     while left + 1 < right:
#         M = (right + left) // 2
#         if a[M] == x:
#             left = M
#         else:
#             right = M
#     if a[right] != a[left]:
#         return left,left
#     else:
#         return left,right
    
    


def predicate(x:int,target:int)->int:
    if  x < target:
        return 0 
    else:
        return 1


def lastOccurence(x:int,target:int)->int:
    if x <= target:
        return 0
    else:
        return 1

def binarySearch(a:list,x:int):
    left,right = 0 , len(a) -1
    while left + 1 < right:
        M = (right + left) // 2
        if predicate(x=a[M],target=x) == 0:
            left = M 
        else:
            right = M 
    while left + 1 < right:
        M = (right + left) // 2
        if lastOccurence(x=a[M],target=x) == 0:
            left = M 
        else:
            right = M 
    return left,right            
            
        
    
    

print(binarySearch(a=arr,x=5))