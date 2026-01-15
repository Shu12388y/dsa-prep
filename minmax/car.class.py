import random

class Car:
    model:str 
    modelNumber:int
    def __init__(self,model,modelNumber) -> None:
        self.model =  model
        self.modelNumber =  modelNumber
        
    
    @classmethod
    def cars(cls):
        cls.modelNumber = 1234
        return cls.modelNumber
    

    @staticmethod
    def generateModel():
        return random.randint(1,10)  
    
    



instance  = Car("Honda",1245) 

print(instance.cars())
print(instance.generateModel())   