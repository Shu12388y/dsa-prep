def findMaxProduct(l:list,k:int):
    init_product,max_product = 1,1
    for i in range(k):
        init_product *= l[i]
    for i in range(k,len(l)-1):
        init_product = int(init_product / l[i-k]) * l[i]
        max_product = max(init_product,max_product)
    print(init_product,max_product)

findMaxProduct([1,2,4,5,10],3) # [8,40]



