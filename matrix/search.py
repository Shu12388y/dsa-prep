mat  = [[1,2,3],[5,6,7],[8,9,10]]

'''
1 2 3
5 6 7
8 9 10

find 6
'''


def search(arr:list,num:int):
    prevpoint = 0
    res = -1
    for i in range(len(arr)):
        for j in range(len(arr)):
            if num > arr[j][i]:
                prevpoint = j 
            break    
    for i in range(prevpoint,len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == num:
                res  = arr[i][j]
                return res
            else:
                res = -1      
    return res


print(search(mat,5))




import sys
input = sys.stdin.readline

def main():
    n, m, x = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    i, j = 0, m - 1  # top-right corner

    while i < n and j >= 0:
        if arr[i][j] == x:
            print("YES")
            return
        elif arr[i][j] > x:
            j -= 1
        else:
            i += 1

    print("NO")

if __name__ == "__main__":
    main()
