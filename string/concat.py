a = [1,2,3]



def main(arr:list)->list:
    res = arr[::] + arr[::]
    print(res)
main(a)