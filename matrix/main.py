

mat = [[1,2,3],[4,5,6],[7,8,9]]

# def printIt(arr):
#     for i in range(len(arr)):
#         if i % 2 == 0:
#             for j in range(len(arr)):
#                 print(arr[i][j])
#         else:
#             for j in reversed(range(len(arr))):
#                 print(arr[i][j])
                
                
# printIt(mat)
# 1,2,3,6,5,4,7,8,9



# def printBoundary(arr):
#     for i in range(len(arr)):
#         if i == 0:
#             for j in range(len(arr)):
#                 print(arr[i][j])
        
#         if i != len(arr)-1 and i != 0:
#             print(arr[i][0])
#             print(arr[i][len(arr)-1])

#         if i == len(arr)-1:
#             for j in range(len(arr)):
#                 print(arr[i][j])
                
                
# printBoundary(mat)
# 1,2,3,4,6,7,8,9



def spiralPrint(arr):
    top,left = 0,0
    bottom,right = len(arr) - 1,len(arr) -1
    for _ in range(len(arr)):
        print(arr[0][left])
        left += 1
        top += 1
    for _ in range(len(arr)):
        print(arr[top - 1][right])
        top -= 1

    for _ in range(len(arr)):
        print(arr[len(arr)-1][right])
        right -= 1
        bottom -= 1
        
    for _ in range(len(arr)):
        print(arr[bottom][left-1])
        left -= 1
spiralPrint(mat)       
     
    