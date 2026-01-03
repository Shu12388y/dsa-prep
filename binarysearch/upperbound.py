# upperbound
# find the first element that is greater than x



arr = [ -1,2,3,4,5,5,5,5,6,8,9]



def predicate(x:int,target:int):
    if x <= target:
        return 0
    else:
        return 1


def binarySearch(a:list,x:int):
    left, right = -1 , len(a)
    while left + 1 < right:
        M = (right + left) // 2
        if predicate(x=a[M],target=x) == 0:
            left = M 
        else:
            right = M 
            
    return a[right]    
    
    
    
print(binarySearch(a=arr,x=-1))