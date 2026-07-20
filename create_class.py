class Car:

    def __init__(self,color:str,mileage:int):
        self.color=color
        self.mileage=mileage

    def display(self):
        print(f"The {self.color} car has {self.mileage:,} miles")    

obj1=Car("blue",20_000)
obj2=Car("red",30_000)
obj1.display()
obj2.display()