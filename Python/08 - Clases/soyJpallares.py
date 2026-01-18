# Ejercicio

class Programmer:

    surname: str = None

    def __init__(self, name: str, age: int, languages: list):
        self.name = name
        self.age = age
        self.languages = languages

    def print(self):
        print(
            f"Nombre: {self.name} | Apellidos: {self.surname} | Edad: {self.age} | Lenguajes: {self.languages}")

my_programmer = Programmer("Jonatan", 45, ["Pascal", "C", "C++", "Cobol", "Visual Basic 6.0", "Visual FoxPro 9.0", "MySQL", "Python", "Java"])
my_programmer.print()
my_programmer.surname = "Pallares"
my_programmer.print()
my_programmer.age = 48
my_programmer.print()