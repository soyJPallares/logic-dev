

#  * EJERCICIO:
#  * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
#  * implemente una superclase Animal y un par de subclases Perro y Gato,
#  * junto con una función que sirva para imprimir el sonido que emite cada Animal.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
#  * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
#  * Cada empleado tiene un identificador y un nombre.
#  * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
#  * actividad, y almacenan los empleados a su cargo.

def Menu():
    print("1. Managemment")
    print("2. Projects Managemment")
    print("3. Development")
    print("0. Quit")



class Employee:
    def __init__(self, id: int, name: str, user: str):
        self.id: int = id
        self.name: str = name
        self.user: str = user
        self.team: list = []



class Manager(Employee):
    def __init__(self, id, name, user, department: str):
        super().__init__(id, name, user)
        self.department: str = department
        self.team: list = []


    def assign_team(self, project_manager: str):
        self.project_manager: str = project_manager
        self.team.append(self.project_manager)


    def print_department(self):
        print(f'Department: {self.department} | Manager: {self.name}')
        print(f'Team: ')

        managers_team: list = []
        for member in range(len(self.team)):
            managers_team.append(self.team[member].name)

        print(managers_team)


    def approvals(self, amount:int, ticket:bool):
        self.amount: int = amount
        self.ticket: bool = ticket
        if self.amount >= 50000 and self.ticket == False: print(f'Amount: {self.amount} | Ticket: {self.ticket} | Bill - "Denied"')
        else: print(f'Amount: {self.amount} | Ticket: {self.ticket} | Bill - "Approved"')



class ProjectManager(Employee):
    def __init__(self, id, name, user, project: str):
        super().__init__(id, name, user)
        self.project: str = project
        self.tasks: dict = {}
        self.team: list = []


    def assign_team(self, programmer: str):
        self.programmer: str = programmer
        self.team.append(self.programmer)


    def print_project(self):
        print(f'Project: {self.project} | Project Manager: {self.name}')
        print(f'Team: ')
        
        programmers_team: list = []
        for member in range(len(self.team)):
            programmers_team.append(self.team[member].name)

        print(programmers_team)


    def assign_tasks(self, programmer: str, task: str):
        self.programmer: str = programmer
        self.task: str = task

        self.tasks[self.programmer] = self.task
        print(f'Programmer: {self.programmer.name} | Task assigned: "{self.task}"')

    # def printType(self):
    #     print(type(self.tasks))


class Programmer(Employee):
    def __init__(self, id, name, user, level: str, language: str):
        super().__init__(id, name, user)
        self.level: str = level
        self.language: str = language


    def commit(self, message: str):
        self.message: str = message
        self.branch: str = self.user
        print(f'Commit: "{self.message}" | Branch: {self.branch} | Programmer: {self.name}')


#--------------------------------------------------------------------------


def main():

    my_mg: Manager = Manager(1, "Joshua Dax", "@jdax", "Operations")

    my_pm_01: ProjectManager = ProjectManager(2, "John Doe", "@jdoe", "AlphaPrime")
    my_pm_02: ProjectManager = ProjectManager(3, "Jane Dox", "@jdox", "BetaTax")

    my_prg_01: Programmer = Programmer(4, "Alice Fox", "@afox", "Senior", "python/FastApi")
    my_prg_02: Programmer = Programmer(5, "Bob Smith", "@bsmith", "Junior", "javascript/React/")
    my_prg_03: Programmer = Programmer(6, "Charlie Brown", "@cbrown", "Mid-level", "html/css")
    my_prg_04: Programmer = Programmer(7, "Diana Prince", "@dprince", "Trainee", "python/FastApi")
    my_prg_05: Programmer = Programmer(4, "Allen Foxter", "@afoxter", "Senior", "python/FastApi")
    my_prg_06: Programmer = Programmer(5, "Bobie Smithson", "@bsmithson", "Junior", "javascript/React/")
    my_prg_07: Programmer = Programmer(6, "Charles Boswell", "@cboswell", "Mid-level", "html/css")
    my_prg_08: Programmer = Programmer(7, "Liv Tyler", "@ltyler", "Trainee", "python/FastApi")
    # my_pm_01.print_type()
    print('--------------------------------------------------------------------------')

    my_mg.assign_team(my_pm_01)
    my_mg.assign_team(my_pm_02)
    my_mg.print_department()
    my_mg.approvals(50000, True)
    my_mg.approvals(60000, False)
    print('--------------------------------------------------------------------------')

    my_pm_01.assign_team(my_prg_01)
    my_pm_01.assign_team(my_prg_02)
    my_pm_01.assign_team(my_prg_03)
    my_pm_01.assign_team(my_prg_04)
    my_pm_01.print_project()
    my_pm_01.assign_tasks(my_prg_01, "Implementar login")
    my_pm_01.assign_tasks(my_prg_02, "Implementar registro")
    my_pm_01.assign_tasks(my_prg_03, "Diseñar Maquetado")
    my_pm_01.assign_tasks(my_prg_04, "Diseñar Base de Datos")
    print('--------------------------------------------------------------------------')

    my_pm_02.assign_team(my_prg_05)
    my_pm_02.assign_team(my_prg_06)
    my_pm_02.assign_team(my_prg_07)
    my_pm_02.assign_team(my_prg_08)
    my_pm_02.print_project()
    my_pm_02.assign_tasks(my_prg_05, "Diseñar Base de Datos / Backend")
    my_pm_02.assign_tasks(my_prg_06, "Implementar login / Middleware")
    my_pm_02.assign_tasks(my_prg_07, "Diseñar Maquetado / Frontend")
    my_pm_02.assign_tasks(my_prg_08, "Diseñar / Implementar API REST")
    print('--------------------------------------------------------------------------')

    my_prg_01.commit("Login implemented")
    my_prg_02.commit("Registration implemented")
    my_prg_03.commit("Layout designed")
    my_prg_04.commit("Database designed")
    print('--------------------------------------------------------------------------')

    my_prg_05.commit("Database designed / Backend implemented")
    my_prg_06.commit("Login implemented / Middleware implemented")
    my_prg_07.commit("Layout designed / Frontend implemented")
    my_prg_08.commit("API REST designed / implemented")

main()
