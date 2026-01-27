"""
Sliding Window

Given an array of size n, lets calculate the maximum sum of k 
consecutive element in the array.

"""



def findMaxN(arr:list, k:int)->int:
    max_sum  = -1
    for i in range(0,len(arr) - k):
        s = 0
        for j in range(i, i + k -1):
            s += arr[j]
        max_sum = max(max_sum,s)
    print(max_sum)
    return 1


def findN(arr: list, k: int):
    i = 0
    result = []
    while i < len(arr) - k:
        current_sum = 0
        for j in range(k):
            if i + j >= len(arr):
                break
            current_sum += arr[i + j]
        result.append(current_sum)
        i += 1
    print(max(result))


# T.C. O(N)
def slidingWindow(arr:list,k:int):
    s,max_sum = 0,0
    for i in range(k):
        s = s + arr[i]
    for i in range(k,len(arr)-1):
        s = s - arr[i - k] + arr[i]
        max_sum = max(s,max_sum)
    print(max_sum)

def main():
    l = [4,3,9,6,7,8] #[16,18,22,21]
    slidingWindow(arr=l,k=3) # T.C O(N*K)




if __name__  == "__main__":
    main()
    
    
'''
To optimize the code, think of 
- what is the repeatitive work I am doning
- How I can avoit it

Where all can the sliding window technique be easily appied

- The operation to be computed is dependent upon the clear complementary
operation kind of scenario (e.g. Addition, subtraction)
- There are scenarios where it is not so easly to applied sliding window
E.g Max in array

'''

