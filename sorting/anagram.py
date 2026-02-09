"""  
Give an array of words, print all anagram together.

I/P: ["care","tap","race","apt","acre"]
O/P: "care race acre tap apt"




"""


def compare(l:str,n:str):
    c  = sorted(l)
    d = sorted(n)
    return c == d

def main(n:list):
    res= []
    for i in n:
        v = sorted(i)
        res.append(v)
    print(res) 
    



if __name__ == "__main__":
    l=["care","tap","race","apt","acre"]
    main(l)