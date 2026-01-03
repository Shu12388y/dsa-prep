# Find the sqaure root of number using any library 
# find sqrt(17)

def predicate(x:int,target:int):
    if x * x <= target:
        return 0
    else:
        return 1

def findSqrt(x):
    left,right = -1, x
    while left + 0.1 < right:
        M =  (right + left) / 2.0
        if predicate(M,x) == 0:
            left = M 
        else:
            right = M
    return right
    


print(findSqrt(x=1/2))
