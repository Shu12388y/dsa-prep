

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



def printBoundary(arr):
    for i in range(len(arr)):
        if i == 0:
            for j in range(len(arr)):
                print(arr[i][j])
        
        if i != len(arr)-1 and i != 0 and i != len(arr):
            for j in range(len(arr)):
                if j == 0 or j == len(arr)-1:
                    print(arr[i][j])

        if i == len(arr)-1:
            for j in range(len(arr)):
                print(arr[i][j])
                
                
printBoundary(mat)
# 1,2,3,4,6,7,8,9