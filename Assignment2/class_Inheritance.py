class Dog:
    species = "Canis familiaris"

    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

    def show(self):
        print(f"{self.name} is {self.age} years old")   
    
    def speak(self, sound):
        print(f"{self.name} says {sound}")
    
class GoldenRetriever(Dog):
   def speak(self,sound="Bark"):
       return super().speak(sound)

obj1 = GoldenRetriever("Puppy",18)
obj1.show()
obj1.speak()  

