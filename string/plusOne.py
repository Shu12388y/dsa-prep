a  = [0]

def main(arr:list)->list:
    res = ''
    pluseOne = 0
    result = []
    for i in arr:
        res += str(i) 
    pluseOne += int(res)
    pluseOne =  pluseOne + 1
    
    for i in str(pluseOne):
        result.append(int(i))
        
    print(result)
    
main(a)    