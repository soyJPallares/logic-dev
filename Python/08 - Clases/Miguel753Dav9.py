class Programmer:
    
    surname: str = None
    def __init__(self, name: str, age: int, lenguage: list):
        self.name = name
        self.age = age
        self.lenguage = lenguage

    def print(self):
            print(
                 f"Nombre: {self.name} | Apellidos: {self.surname} | Edad: {self.age} | Lenguajes: {self.lenguage}")

my_programmer = Programmer("Miguel", 11, ["Python", "Java"])
my_programmer.print()
my_programmer.surname = "Pallares"
my_programmer.print()
my_programmer.age = 12
my_programmer.print()