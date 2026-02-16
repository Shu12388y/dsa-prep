''' 
    Framework

 - State
 - Transition
 - Base Case



State - what are the parameter that our problem depend on

f(n) -> Return nth fib. no.

'''



def printN(n):
    if n == 0:
        return
    # print("called",n)
    return printN(n -1)


printN(5)