"""

Here are trains and every train stops at stations 

t1 = [s2,s3,s4]
t2 = [s3,s4,s5]
t3 = [s1,s2]
t4 = [s1,s2,s3,s4,s5]
t5 = [s4,s5]


Find the most popular station

There are m stations and n trains


"""


# T.C. O(n*m) S.C = O(Number of station)
def find_the_mosts_popular_station(station:list[list]): 
    fre = [0]*6  
    for i in station:
        for s in i:
            fre[s] += 1
    print(max(fre))
    
 
 
# T.C. O(n+m)
# Lazy Propagation

def find_station(station:list[list]):
    fre = [0] * 5
    res = [1]* 5
    for i in station:
        fre[i[0]] += 1
        if len(fre) <= i[1]+1:
            continue
        else:
            fre[i[1]+1] -= 1
        
    res[0] = fre[0]
    for i in range(1,len(fre)):
        res[i] = res[i-1] + fre[i] 
    print(res)
        

m = [
    [2,4],
    [3,5],
    [1,2],
    [1,5],
    [4,5]
]


m1 = [
    [1,3],
    [2,4],
    [0,1],
    [0,4],
    [3,4]
]

# find_the_mosts_popular_station(m)
find_station(m1)

