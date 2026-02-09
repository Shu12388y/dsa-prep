"""
What is sorting?
Rearranging item in a specific order


Different type of sorting
1.  Bubble sort
2.  Insertion sort
3.  Selection sort
4.  Merge Sort
5.  Quick Sort
6.  Heap Sort
"""


"""
Given an unsorted array of interger,
sort the array in wave array


a[0]>=a[1]<=a[2]>=a[3]<=a[4]


i/p: [12,99,29,11,41]
        [11,12,29,41,99]
o/p: [41,12,29,11,99]

"""

def main(n:list):
   minp,maxp = 0,len(n) - 1
   l = sorted(n)
   while maxp  >= minp:
       print(l[maxp])
       print(l[minp])
       minp += 1
       maxp -= 1


if __name__ == "__main__":
    a = [12,99,29,11,41]
    main(a)