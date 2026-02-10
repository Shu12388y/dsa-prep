"""   
10
2 3 11 10 8 5 0 12 4 6

sorted = 0 2 3 4 5 6 8 10 11 12

"""




def main():
    l = [0, 2, 3, 4, 5, 6, 8, 10, 11, 12]
    p = 0
    t = 0
    total = 0
    for i in range(len(l)-1):
        if l[i +1 ] - l[i] == 1:
            p = i 
            break   
        else:
            i += 1
            
    for j in range(1,len(l)):
        if p + j == l[j]:
             
    
    
    
    
if __name__ == "__main__":
    main()