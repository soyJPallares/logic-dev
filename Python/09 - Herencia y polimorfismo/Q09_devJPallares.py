

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


#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
class Employee:
    def __init__(self, id: int, name: str, user: str):
        self.id: int = id
        self.name: str = name
        self.user: str = user
        self.team: list = []

#-------------------------------------
    def add_team_member(self, member):
        self.team.append(member)

#-------------------------------------
    def print_team(self):
        print(f'Team: ')
        for member in self.team: print(member.name)


#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
class Manager(Employee):
    def __init__(self, id, name, user, department: str):
        super().__init__(id, name, user)
        self.department: str = department

#-------------------------------------
    def print_department(self):
        print(f'Department: {self.department} | Manager: {self.name}')
        print(f'The {self.department} department manager, {self.name}, is managing the projects ')

#-------------------------------------
    def approvals(self, amount:int, ticket:bool):
        self.amount: int = amount
        self.ticket: bool = ticket
        if self.amount >= 50000 and self.ticket == False: print(f'Amount: {self.amount} | Ticket: {self.ticket} | Bill - "Denied"')
        else: print(f'Amount: {self.amount} | Ticket: {self.ticket} | Bill - "Approved"')


#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
class ProjectManager(Employee):
    def __init__(self, id, name, user, project: str):
        super().__init__(id, name, user)
        self.project: str = project
        self.tasks: dict = {}

#-------------------------------------
    def print_project(self):
        print(f'Project: {self.project} | Project Manager: {self.name}')

#-------------------------------------
    def assign_tasks(self, programmer: str, task: str):
        self.programmer: str = programmer
        self.task: str = task

        self.tasks[self.programmer] = self.task
        print(f'Programmer: {self.programmer.name} | Task assigned: "{self.task}"')



#--------------------------------------------------------------------------
class Programmer(Employee):
#--------------------------------------------------------------------------
    def __init__(self, id, name, user, level: str, language: str):
        super().__init__(id, name, user)
        self.level: str = level
        self.language: str = language

#-------------------------------------
    def add_team_member(self, member:Employee):
        print(f"Un programador no tiene empleados a su cargo. {member.name} no se añadirá.")

#-------------------------------------
    def commit(self, message: str):
        self.message: str = message
        self.branch: str = self.user
        print(f'Commit: "{self.message}" | Branch: {self.branch} | Programmer: {self.name}')

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
def Menu():
    print("1. Managemment")
    print("2. Projects Managemment")
    print("3. Development")
    print("0. Quit")


def main():

    my_manager: Manager = Manager(1, "Joshua Dax", "@jdax", "Operations")

    my_project_manager_01: ProjectManager = ProjectManager(2, "John Doe", "@jdoe", "AlphaPrime")
    my_project_manager_02: ProjectManager = ProjectManager(3, "Jane Dox", "@jdox", "BetaTax")

    my_programmer_01: Programmer = Programmer(4, "Alice Fox", "@afox", "Senior", "python/FastApi")
    my_programmer_02: Programmer = Programmer(5, "Bob Smith", "@bsmith", "Junior", "javascript/React/")
    my_programmer_03: Programmer = Programmer(6, "Charlie Brown", "@cbrown", "Mid-level", "html/css")
    my_programmer_04: Programmer = Programmer(7, "Diana Prince", "@dprince", "Trainee", "python/FastApi")
    my_programmer_05: Programmer = Programmer(4, "Allen Foxter", "@afoxter", "Senior", "python/FastApi")
    my_programmer_06: Programmer = Programmer(5, "Bobie Smithson", "@bsmithson", "Junior", "javascript/React/")
    my_programmer_07: Programmer = Programmer(6, "Charles Boswell", "@cboswell", "Mid-level", "html/css")
    my_programmer_08: Programmer = Programmer(7, "Liv Tyler", "@ltyler", "Trainee", "python/FastApi")
    # my_project_manager_01.print_type()
    print('--------------------------------------------------------------------------')

    my_manager.add_team_member(my_project_manager_01)
    my_manager.add_team_member(my_project_manager_02)
    my_manager.print_department()
    my_manager.print_team()

    my_manager.approvals(45000, False)
    my_manager.approvals(60000, False)
    my_manager.approvals(90000, True)
    print('--------------------------------------------------------------------------')

    my_project_manager_01.print_project()
    my_project_manager_01.add_team_member(my_programmer_01)
    my_project_manager_01.add_team_member(my_programmer_02)
    my_project_manager_01.add_team_member(my_programmer_03)
    my_project_manager_01.add_team_member(my_programmer_04)
    my_project_manager_01.print_team()

    my_project_manager_01.assign_tasks(my_programmer_01, "Implementar login")
    my_project_manager_01.assign_tasks(my_programmer_02, "Implementar registro")
    my_project_manager_01.assign_tasks(my_programmer_03, "Diseñar Maquetado")
    my_project_manager_01.assign_tasks(my_programmer_04, "Diseñar Base de Datos")
    print('--------------------------------------------------------------------------')
    my_programmer_01.add_team_member(my_programmer_02)
    print('--------------------------------------------------------------------------')

    my_project_manager_02.print_project()
    my_project_manager_02.add_team_member(my_programmer_05)
    my_project_manager_02.add_team_member(my_programmer_06)
    my_project_manager_02.add_team_member(my_programmer_07)
    my_project_manager_02.add_team_member(my_programmer_08)
    my_project_manager_02.print_team()

    my_project_manager_02.assign_tasks(my_programmer_05, "Diseñar Base de Datos / Backend")
    my_project_manager_02.assign_tasks(my_programmer_06, "Implementar login / Middleware")
    my_project_manager_02.assign_tasks(my_programmer_07, "Diseñar Maquetado / Frontend")
    my_project_manager_02.assign_tasks(my_programmer_08, "Diseñar / Implementar API REST")
    print('--------------------------------------------------------------------------')

    my_programmer_01.commit("Login implemented")
    my_programmer_02.commit("Registration implemented")
    my_programmer_03.commit("Layout designed")
    my_programmer_04.commit("Database designed")
    print('--------------------------------------------------------------------------')

    my_programmer_05.commit("Database designed / Backend implemented")
    my_programmer_06.commit("Login implemented / Middleware implemented")
    my_programmer_07.commit("Layout designed / Frontend implemented")
    my_programmer_08.commit("API REST designed / implemented")

main()
