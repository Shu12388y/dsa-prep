'''
find the number that is bigger than sum of i numbers
1,2,3,4,...,i < N


for example: [1,2,3,4,5,6,7] , N = 5 + 1 = 6/2= 3 -> 1,2,3

let N = 8 -> 8 + 1 = 9/2 = 4
'''



# def predicate(ip:int,target:int):
#     n = (target + 1) // 2
#     if ip < n:
#         return 0
#     else:
#         return 1


# def findMaxN(arr:list,N:int):
#     left, right = -1, len(arr)
#     while left + 1 < right:
#         m = (right + left) // 2
#         if predicate(arr[m],N) == 0:
#             left = m
#         else:
#             right = m

#     return arr[right]


# print(findMaxN(arr=[1,2,3,4,5,6,8],N=10))

'''
N = 10
10 + 1 = 11 // 2 = 5
1 + 2 + 3 + 4 + 5 = 15 

'''
    
    
    
    
def predicate(m:int,n:int):
    if ((m*(m+1))/ 2 <= n):
        return 0 
    else:
        return 1
    

def findMaxN(arr:list,n:int):
    left, right = 0, len(arr)
    if left + 1 < right:
        m = (right + left) // 2
        if predicate(arr[m],n) == 0:
            left = m 
        else:
            right = m 
    return left, right


print(findMaxN(arr=[1,2,3,4,5,6,7],n=5))
# 1 + 2 + 3 + 4 = 10
# 4(4 + 1) / 2 = 4 * 5 / 2 = 10 