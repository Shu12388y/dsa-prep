class Arrays:
    _vals:list
    def __init__(self,val:list) -> None:
        self._vals = val
        
        
    
    def getlist(self):
        return self._vals    
        
    @classmethod
    def iterators(cls,fn):
        for i in range(len(cls._vals)):
            fn(cls._vals[i])
        