

mat = [[1,2,3],[4,5,6],[7,8,9]]

def printIt(arr):
    for i in range(len(arr)):
        if i % 2 == 0:
            for j in range(len(arr)):
                print(arr[i][j])
        else:
            for j in reversed(range(len(arr))):
                print(arr[i][j])
                
                
printIt(mat)
# 1,2,3,6,5,4,7,8,9