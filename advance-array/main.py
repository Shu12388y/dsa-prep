"""
Sliding Window

Given an array of size n, lets calculate the maximum sum of k 
consecutive element in the array.
"""



def findN(arr: list, k: int):
    i = 0
    result = []
    while i < len(arr):
        current_sum = 0
        for j in range(k):
            if i + j >= len(arr):
                break
            current_sum += arr[i + j]
        result.append(current_sum)
        i += 1

    print(max(result))




def main():
    l = [4,3,9,6,7,8] #[16,18,22,21]
    findN(arr=l,k=3)

if __name__  == "__main__":
    main()