'''
Given n piles of stones (array is not sorted)

[1,3,2,4]

h is given, h = 5.(number of operation)


Every time  - select 1 pile at
- remove at max k stone from the pile

Goal: Empty the piles in <=h operation


Find a min k that achieve the goal of the game


if k = 2
[1,2,1,2] = 6 (failed) 


if k = 3
[1,1,1,2] = 5 (done)

if k = 4
[1,1,1,1] = 4 (done)
 
'''


# def predicate(n:int,maxn:int):
#     if maxn > n:
#         return 0
#     else:
#         return 1
        
    
# def stone(arr:list,h:int):
#     sortedList = sorted(arr)
#     maxNums = max(sortedList) - 1
#     left, right = -1, len(arr)
#     while(left + 1< right):
#         m = (right + left) // 2
#         if predicate(sortedList[m],maxn=maxNums) == 0:
#             left = m 
#         else:
#             right = m 
#     return sortedList[right]    



# print(stone(arr=[1,3,2,4],h=5))


def predicate(m:int,n:int,arr:list,k:int)->int:
    nops = 0
    for i in range(0,n):
        ops = (arr[i] + m -1 )/m
        nops += ops 
    if(nops <= k):
        return 1 
    else:
        return 0


def rock(arr:list,k:int):
    left, right = 0, max(arr)
    while (left + 1 < right):
        m = left + (right - left) // 2
        if  predicate(m=arr[m],n=len(arr),k=k,arr=arr) == 0:
            left = m 
        else:
            right  = m
    return right


print(rock(arr=[1,3,2,4],k=5))