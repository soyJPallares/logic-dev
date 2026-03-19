# Create the Animal class
class Animal:
    # Constructor
    def __init__(self, name:str):
        self.name: str = name

    # Method
    def sound(self):
        print("Hago un sonido")

# Create the Dog class (inherits from Animal)
class Dog(Animal):

    # def __init__(self, name:str):
    #    self.name: str = name
    
    def sound(self):
        print("Woof")

# Create the Cat class
class Cat(Animal):
  
    # def __init__(self, name:str):
    #     self.name: str = name

    def sound(self):
        print("Meow")

# Create the Fox class
class Fox(Animal):
    pass

    # def __init__(self, name:str):
    #     self.name: str = name

#   def sound(self):
#     print("Wa-pa-pa-pa-pa-pow!")

# Create objects and loop
c1 = Cat("gatito")
d1 = Dog("Rex")
f1 = Fox("Foxy")

for animal in (c1, d1, f1):
  animal.sound()

  