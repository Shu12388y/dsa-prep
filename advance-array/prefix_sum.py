def prefixSum(l:list)->None:
    init = 0
    res_list = []
    for i in range(len(l)):
        init += l[i]
        res_list.append(init)
    # print(res_list)


k = [1,2,3,2,4]
r = [3,4,8,-1,-2,4,6,7]

"""
k = [1,2,3,2,4]
[1,3,6,8,12]
"""
prefixSum(r)



def newPrefix(l):
    prefix = [1] * len(l)
    prefix[0] = l[0]
    for i in range(1,len(l)):
        prefix[i] = prefix[i-1] + l[i]
    # print(prefix)
newPrefix(k)



"""
Range of queries

N = [3,4,8,-1,-2,4,6,7]


There are queries of type [l,r]. You need to give
sum of each query inclusive of L & R are indices


Q = [3,5]

"""



def findPrefixSum(l:list,q:list):
    prefix_sum  = [1] * len(l)
    prefix_sum[0] = l[0]
    res = 0
    for i in range(1,len(l)):
        prefix_sum[i] = prefix_sum[i - 1] + l[i]
    res = prefix_sum[q[1]] - prefix_sum[q[0]-1]
    print(res)         
    

# q = [2,4]

# q = [1,3]
q = [2,4]

findPrefixSum(k,q)


"""

k = [1,2,3,2,4]
q = [1,3]
res = 2+3+2 = 7
[1, 3, 6, 8, 12]

q = [1,4]
res = 2+3+2+4 = 11


q = [2,4]
res = 3+2+4 = 9 
"""

