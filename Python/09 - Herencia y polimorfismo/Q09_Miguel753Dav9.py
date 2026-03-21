"""
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
"""
def Menu():
    print("1. Gerente")
    print("2. Gerente de proyectos")
    print("3. Programador")
    print("0. Salir")


class Employee:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class Manager(Employee):
    def __init__(self, id, name, departamento):
        super().__init__(id, name)
        self.departament = departamento

    def aprobar_gasto(self, monto):
        self.monto = monto
        if self.monto >= 50000:
            print("Gasto denegado")
        else:
            print("Gasto aprobado")    

class ProjectManager(Employee):
    def __init__(self, id, name, proyecto):
        super().__init__(id, name)
        self.project = proyecto
        self.tasks: dict = {}

    def asignar_tarea(self, programmer, task):
        self.programmer = programmer
        self.task = task

    # def printType(self):
    #     print(type(self.tasks))

class Programmer(Employee):
    def __init__(self, id, name, lenguajes, nivel):
        super().__init__(id, name)
        self.lenguage = lenguajes
        self.level = nivel

    def hacer_commit(self, menssage, branch):
        pass
