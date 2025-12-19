s = '0011'


def main():
    res = []
    stm= ''
    strMap = {
        '00':'A',
        '01':'T',
        '10':'C',
        '11':'G'
    }
    for i in range(len(s)):
        if i % 2 == 0:
            res.append(s[i:i+2])

    for i in res:
        if strMap[i]:
          stm += strMap[i]
          
    print(stm)  

    
if __name__ == "__main__":
    main()    