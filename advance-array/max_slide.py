def findMax(l:list, k=1):
    max_num,sec_num = 0,0
    for i in range(k):
        max_num = max(max_num,l[i])
    for i in range(k,len(l)):
        sec_num = max(sec_num,l[i])
        max_num = max(sec_num,max_num)
    print(max_num)
    
    
    
findMax([3,4,7,8,9,3,12],3)