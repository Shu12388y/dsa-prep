mat = [[1,2,3],[4,5,6],[7,8,9]]



# def transpose(arr:list):
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if i < j:
#                 arr[i][j],arr[j][i] = arr[j][i] ,arr[i][j]
#     print(arr)
    
# transpose(mat)    

            
# Rotate a matrix


def rotate(arr:list):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i < j:
                arr[i][j],arr[j][i] = arr[j][i],arr[i][j]
                
    for j in range(len(arr)):
        top, bottom = 0, len(arr) - 1
        while top < bottom:
            arr[top][j], arr[bottom][j] = arr[bottom][j], arr[top][j]
            top += 1
            bottom -= 1
    print(arr)
            
rotate(mat)
            