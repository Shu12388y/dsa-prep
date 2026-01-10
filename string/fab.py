# 0,1,1,2,3,5
# n m p
def series(nums:int):
    n = 0
    i = 0 
    m = 1
    print(n)
    while i < nums:
        prev = n + m 
        m = n
        n= prev
        print(prev)
        i += 1
        
series(5) 
        
        