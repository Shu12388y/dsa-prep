class Vechile:
    name:str
    def __init__(self,name) -> None:
        self.name = name
        
    
    def getName(self):
        self.name = "Ford"    
    
    @staticmethod
    def changeName():
        return "Static Method"
        