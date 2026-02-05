"""
Prefix sum of matrix 

1,2,3
4,5,6
7,8,9



prefix sum

1,3,3
7,12,6
7,8,9


find the prefix upto 5

It will be
1+2+4+5

"""



def find_index(k:int,m:list[list]):
    for i in range(len(m)):
        for j in range(i,len(m)):
            if m[i][j] == k:
                return i,j         
    else:
        return -1,-1
        



def prefix_sum(m:list[list],n:int):
    i,j = find_index(n,m)
    ref = m.copy()    
    for t in range(0,i+1):
        for o in range(0,j+1):
            ref[t+1][o+1] = ref[t+1][o+1] + m[o][t]
    
    print(ref)
    
    
m=[[1,2,3],[4,5,6],[7,8,9]]    

prefix_sum(m,5)