"""  
3
2 1
8 3
5 7


There are three cows

1 - arrive at 2s and checking is 1s -> 1 => 3s
2 - arrive at 5s and checking is 7s ->  7 => 12s
3 - arrive at 8s and checking is 3s ->  3 => 11s 

start 2 
checking 1 -> 3

start 3  but cow arrive at 5 
checking 7 -> 5 + 7 = 12

start 12
checking 3 -> 15

"""


import sys

def main():
    input = sys.stdin.readline

    n = int(input())
    cows = []

    for _ in range(n):
        a, b = map(int, input().split())
        cows.append((a, b))

    # Sort cows by arrival time
    cows.sort()

    current_time = 0

    for a, b in cows:
        current_time = max(current_time, a) + b

    print(current_time)

if __name__ == "__main__":
    main()

    