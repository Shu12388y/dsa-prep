def findMaxProduct(l:list,k:int):
    init_product,max_product = 1,1
    for i in range(k):
        if l[i] == 0:
            continue
        init_product *= l[i]
    for i in range(k,len(l)-1):
        if l[i] == 0:
            init_product = int(init_product / l[i-k])
            max_product = max(init_product,max_product)
        else:
            init_product = int(init_product / l[i-k]) * l[i]
            max_product = max(init_product,max_product)
    print(init_product,max_product)

findMaxProduct([1,2,0,4,5,10],3) 

# 2 , 8, 20, 200


"""
def findMaxProduct(l, k):
    product = 1
    zero_count = 0
    max_product = 0

    for i in range(len(l)):
        if l[i] == 0:
            zero_count += 1
        else:
            product *= l[i]

        if i >= k:
            if l[i - k] == 0:
                zero_count -= 1
            else:
                product //= l[i - k]

        if i >= k - 1 and zero_count == 0:
            max_product = max(max_product, product)

    print(max_product)

"""
