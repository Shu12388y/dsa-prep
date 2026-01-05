"""
Minmax array

"""

class Array:
    val = []
    def __init__(self,v:list):
        self.val = v 
    
    def sortit(self):
        return sorted(self.val)



lt = Array([12,5,31,3,2,0])
print(lt.sortit())
    
    

        

