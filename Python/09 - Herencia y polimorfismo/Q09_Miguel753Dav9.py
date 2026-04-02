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
    def __init__(self, id: int, name: str, user: str):
        self.id = id
        self.name = name
        self.user = user
        self.team = []

    def add_team_member(self, member):
        self.team.append(member)

    def print_team(self):
        print(f'Team: ')
        for member in self.team: print(member.name)


class Manager(Employee):
    def __init__(self, id, name, user, departamento):
        super().__init__(id, name, user)
        self.departament = departamento

    def aprobar_gasto(self, monto):
        self.monto = monto
        if self.monto >= 50000:
            print("Gasto denegado")
        else:
            print("Gasto aprobado")

    def print_department(self):
        print(f'Departamento: {self.departament} | Gerente: {self.name}')
        print(f'El gerente del departamento {self.departament}, {self.name}, esta administrando el proyecto.')

    def menuManager(self):
        print("1. Aprobacion de gasto")
        print("2. Imprimir el departamento")
        print("0. Salir")

class ProjectManager(Employee):
    def __init__(self, id, name, user, proyecto):
        super().__init__(id, name, user)
        self.project = proyecto
        self.tasks: dict = {}

    def asignar_tarea(self, programmer, task):
        self.programmer = programmer
        self.task = task

        self.tasks[self.programmer] = self.task
        print(f'Programador: {self.programmer.name} | Tarea asignada: "{self.task}"')


    def printProject(self):
        print(f"Proyecto: {self.project} | Gerente del proyecto {self.name}")

    def menuProject(self):
        print("1. Gerente de proyecto 1")
        print("2. Gerente de proyecto 2")
        print("0. Salir")

    def menuManagerProject(self):
        print("1. Asignar tarea")
        print("2. Imprimir el proyecto")
        print("0. Salir")

    # def printType(self):
    #     print(type(self.tasks))

class Programmer(Employee):
    def __init__(self, id, name, user, lenguajes, nivel):
        super().__init__(id, name, user)
        self.lenguage = lenguajes
        self.level = nivel

    def menu_Programmer():
        print("1. Hacer commit")
        print("0. Salir")

    def add_team_member(self, member:Employee):
        print(f"Un programador no tiene empleados a su cargo. {member.name} no se añadirá.")

    def hacer_commit(self, menssage):
        self.menssage: str = menssage
        self.branch: str = self.user
        print(f'Commit: "{self.menssage}" | Branch: {self.branch} | Programador: {self.name}')


my_manager: Manager = Manager(1, "Joshua Dax", "@jdax", "Operations")

my_project_manager_01: ProjectManager = ProjectManager(2, "John Doe", "@jdoe", "AlphaPrime")
my_project_manager_02: ProjectManager = ProjectManager(3, "Jane Doe", "@jdoe", "BetaTax")

my_programmer_01: Programmer = Programmer(4, "Toby Fox", "@tfox", "Senior", "python/FastApi")
my_programmer_02: Programmer = Programmer(5, "Bob Smith", "@bsmith", "Junior", "javascript/React/")
my_programmer_03: Programmer = Programmer(6, "Charlie Brown", "@cbrown", "Mid-level", "html/css")
my_programmer_04: Programmer = Programmer(7, "Diana Prince", "@dprince", "Trainee", "python/FastApi")
my_programmer_05: Programmer = Programmer(4, "Allen Foxter", "@afoxter", "Senior", "python/FastApi")
my_programmer_06: Programmer = Programmer(5, "Bobie Smithson", "@bsmithson", "Junior", "javascript/React/")
my_programmer_07: Programmer = Programmer(6, "Charles Boswell", "@cboswell", "Mid-level", "html/css")
my_programmer_08: Programmer = Programmer(7, "Liv Tyler", "@ltyler", "Trainee", "python/FastApi")
# my_project_manager_01.print_type()

my_manager.add_team_member(my_project_manager_01)
my_manager.add_team_member(my_project_manager_02)

my_project_manager_01.add_team_member(my_programmer_01)
my_project_manager_01.add_team_member(my_programmer_02)
my_project_manager_01.add_team_member(my_programmer_03)
my_project_manager_01.add_team_member(my_programmer_04)

my_project_manager_02.printProject()
my_project_manager_02.add_team_member(my_programmer_05)
my_project_manager_02.add_team_member(my_programmer_06)
my_project_manager_02.add_team_member(my_programmer_07)
my_project_manager_02.add_team_member(my_programmer_08)

my_project_manager_02.asignar_tarea(my_programmer_05, "Diseñar Base de Datos / Backend")
my_project_manager_02.asignar_tarea(my_programmer_06, "Implementar login / Middleware")
my_project_manager_02.asignar_tarea(my_programmer_07, "Diseñar Maquetado / Frontend")
my_project_manager_02.asignar_tarea(my_programmer_08, "Diseñar / Implementar API REST")

my_programmer_01.hacer_commit("Login implemented")
my_programmer_02.hacer_commit("Registration implemented")
my_programmer_03.hacer_commit("Layout designed")
my_programmer_04.hacer_commit("Database designed")

my_programmer_05.hacer_commit("Database designed / Backend implemented")
my_programmer_06.hacer_commit("Login implemented / Middleware implemented")
my_programmer_07.hacer_commit("Layout designed / Frontend implemented")
my_programmer_08.hacer_commit("API REST designed / implemented")

while True:
    Menu()
    opc = int(input("Escoge una opcion: "))
    match opc:
        case 1:
            while True:
                my_manager.menuManager
                opc1 = int(input("Escoge una opcion: "))
                match opc1:
                    case 1:
                        monto = input("Digite el monto (no puede ser maximo de 50.000): ")
                        my_manager.aprobar_gasto(monto)
                    case 2:
                        my_manager.print_department()
                    case 0:
                        break
        case 2:
            while True:
                my_project_manager_01.menuProject()
                opc2 = int(input("Escoge una opcion: "))
                match opc2:
                    case 1:
                        while True:
                            my_project_manager_01.menuManagerProject()
                            opc3 = int(input("Escoge la opcion: "))
                            match opc3:
                                case 1:
                                    Programador = input("Ingrese el programador: ")
                                    valor = globals()[Programador]
                                    Tarea = input("Ingrese la tarea a asignar: ")
                                    my_project_manager_01.asignar_tarea(valor, Tarea)
                                case 2:
                                    my_project_manager_01.printProject()
                                case 0:
                                    break
                    case 2:
                        while True:
                            my_project_manager_01.menuManagerProject()
                            opc3 = int(input("Escoge la opcion: "))
                            match opc3:
                                case 1:
                                    Programador = input("Ingrese el programador: ")
                                    valor = globals()[Programador]
                                    Tarea = input("Ingrese la tarea a asignar: ")
                                    my_project_manager_02.asignar_tarea(valor, Tarea)
                                case 2:
                                    my_project_manager_02.printProject()
                                case 0:
                                    break

        case 3:
            while True:
                my_programmer_01.menu_Programmer()
                opc4 = int(input("Digite la opcion: "))
                match opc4:
                    case 1:
                        Programador2 = input("Ingrese su nombre para continuar: ")
                        commit = input("Digite el commit que quiere hacer: ")
                        valor2 = globals()[Programador2]
                        valor2.hacer_commit(commit)
                    case 0:
                        break
        case 0:
            break