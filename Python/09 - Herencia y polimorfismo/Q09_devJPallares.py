
'''
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
#  * actividad, y almacenan los empleados a su cargo.'''


#--------------------------------------------------------------------------
#  Primary Class Employee
#--------------------------------------------------------------------------
class Employee:
#--------------------------------------------------------------------------
    def __init__(self, id: int, name: str, user: str) -> None:
        self.id: int = id
        self.name: str = name
        self.user: str = user
        self.team: list = []

#-------------------------------------
    def add_team_member(self, member: Employee) -> None:
        self.team.append(member)

#-------------------------------------
    def select_member_team(self, member: Employee) -> Employee:
        self.member: Employee = member
        return self.member

#-------------------------------------
    def print_team(self) -> None:
        print(f'Team members: ')
        for member in self.team: print(f'{member.id} - {member.name} - {member.user}')


#--------------------------------------------------------------------------
#  Hinheritance Class Manager
#--------------------------------------------------------------------------
class Manager(Employee):
#--------------------------------------------------------------------------
    def __init__(self, id, name, user, department: str) -> None:
        super().__init__(id, name, user)
        self.department: str = department
        self.expenses: list = []

#-------------------------------------
    def print_department(self) -> None:
        print(f'Department: {self.department} | Manager: {self.name}')
        print(f'The {self.department} department manager, {self.name}, is managing the projects ')

#-------------------------------------
    def approvals(self, amount: float, ticket: bool) -> None:
        self.amount: float = amount
        self.ticket: bool = ticket

        if self.amount > 50000 and self.ticket == False: self.expenses.append((self.amount, self.ticket, "Denied"))
        else: self.expenses.append((self.amount, self.ticket, "Approved"))

#-------------------------------------
    def print_approvals(self) -> None:
        print(f'Expense approvals for Manager: {self.name} | Department: {self.department}')
        for amount, ticket, status in self.expenses:
            print(f'Amount: {amount:.1f} | Has Ticket: {"Si" if ticket else "No"} | Bill - "{status}"')

#-------------------------------------
    def menuManager(self) -> None:
        print("1. Approval expenses")
        print("2. Print Approvals history")
        print("3. Print department team")
        print("0. Return")

#--------------------------------------------------------------------------
#  Hinheritance Class Project Manager
#--------------------------------------------------------------------------
class ProjectManager(Employee):
#--------------------------------------------------------------------------
    def __init__(self, id, name, user, project: str) -> None:
        super().__init__(id, name, user)
        self.project: str = project
        self.tasks: dict = {}

#-------------------------------------
    def print_project(self) -> None:
        print(f'Project: {self.project} | Project Manager: {self.name}')

#-------------------------------------
    def assign_tasks(self, programmer: str, task: str) -> None:
        self.programmer: str = programmer
        self.task: str = task

        self.tasks[self.programmer] = self.task
        # print(f'Programmer: {self.programmer.name} | Task assigned: "{self.task}"')

# #-------------------------------------
#     def menuProject(self, my_manager: Manager) -> Manager:
#         self.my_manager: Manager = my_manager
#         self.my_manager.print_team()
#         print("0. Return")
#         return self.my_manager

#-------------------------------------
    def menuProjectManager(self) -> None:
        print("1. Print the project")
        print("2. Assign task")
        print("3. Team assigned tasks")
        print("0. Return")


#--------------------------------------------------------------------------
#  Hinheritance Class Programmer
#--------------------------------------------------------------------------
class Programmer(Employee):
#--------------------------------------------------------------------------
    def __init__(self, id, name, user, level: str, language: str) -> None:
        super().__init__(id, name, user)
        self.level: str = level
        self.language: str = language

#-------------------------------------
    def add_team_member(self, member:Employee) -> None:
        print(f"Un programador no tiene empleados a su cargo. \nNo se creará un equipo y {member.name} no se añadirá.")

#-------------------------------------
    def commit(self, message: str) -> None:
        self.message: str = message
        self.branch: str = self.user
        print(f'Commit: "{self.message}" | Branch: {self.branch} | Programmer: {self.name}')

#-------------------------------------
    def menu_Programmer(self) -> None:
        print("1. Commit")
        print("0. Return")

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
def Menu() -> None:
    print("1. Managemment")
    print("2. Projects Managemment")
    print("3. Development")
    print("0. Quit")


def main() -> None:
    # Creando el Gerente
    my_manager: Manager = Manager(1, "Joshua Dax", "@jdax", "Operations")

    # Creando los Gerentes de Proyecto
    my_project_manager_01: ProjectManager = ProjectManager(2, "John Doe", "@jdoe", "AlphaPrime")
    my_project_manager_02: ProjectManager = ProjectManager(3, "Jane Dox", "@jdox", "BetaTax")

    # Creando los Programadores
    my_programmer_01: Programmer = Programmer(4, "Alice Fox", "@afox", "Senior", "python/FastApi")
    my_programmer_02: Programmer = Programmer(5, "Bob Smith", "@bsmith", "Junior", "javascript/React/")
    my_programmer_03: Programmer = Programmer(6, "Charlie Brown", "@cbrown", "Mid-level", "html/css")
    my_programmer_04: Programmer = Programmer(7, "Diana Prince", "@dprince", "Trainee", "python/FastApi")
    my_programmer_05: Programmer = Programmer(4, "Allen Foxter", "@afoxter", "Senior", "python/FastApi")
    my_programmer_06: Programmer = Programmer(5, "Bobie Smithson", "@bsmithson", "Junior", "javascript/React/")
    my_programmer_07: Programmer = Programmer(6, "Charles Boswell", "@cboswell", "Mid-level", "html/css")
    my_programmer_08: Programmer = Programmer(7, "Liv Tyler", "@ltyler", "Trainee", "python/FastApi")
    # my_project_manager_01.print_type()
    # print('--------------------------------------------------------------------------')

    # Asignando los Gerentes de Proyecto al equipo del Gerente General
    my_manager.add_team_member(my_project_manager_01)
    my_manager.add_team_member(my_project_manager_02)

    # Imprime el departamento y el gerente general
    # my_manager.print_department()

    # Imprime el equipo del gerente general (Los gerentes de proyecto que tiene asignados)
    # my_manager.print_team()

    # Probando el sistema de aprobaciones del gerente general
    # Se aprueban gastos menores a 50.000 sin ticket, y se rechazan gastos mayores a 50.000 sin ticket
    # Se aprueban gastos de cualquier monto si cuentan con ticket
    # El módulo imprime inmediatamente el resultado de cada aprobación
    my_manager.approvals(45000, False)
    my_manager.approvals(60000, False)
    my_manager.approvals(90000, True)
    # print('--------------------------------------------------------------------------')

    # Imprime el nombre del proyecto y el gerente del proyecto 01
    # my_project_manager_01.print_project()
    
    # Asignando los programadores al equipo del Proyecto / Gerente de Proyecto
    my_project_manager_01.add_team_member(my_programmer_01)
    my_project_manager_01.add_team_member(my_programmer_02)
    my_project_manager_01.add_team_member(my_programmer_03)
    my_project_manager_01.add_team_member(my_programmer_04)

    # Imprime el equipo del Proyecto (Los programadores asignados al Gerente del proyecto)
    # my_project_manager_01.print_team()

    # Asignando tareas a los programadores desde el Gerente del Proyecto
    my_project_manager_01.assign_tasks(my_programmer_01, "Implementar login")
    my_project_manager_01.assign_tasks(my_programmer_02, "Implementar registro")
    my_project_manager_01.assign_tasks(my_programmer_03, "Diseñar Maquetado")
    my_project_manager_01.assign_tasks(my_programmer_04, "Diseñar Base de Datos")
    #print('--------------------------------------------------------------------------')

    # Prueba de Asignación de programador fallida,
    # Los programadores no pueden tener asiggnados a otros programadores
    # El sistema lo indicará y NO se añadirá un programador a un equipo de otro programador
    # my_programmer_01.add_team_member(my_programmer_02)
    # print('--------------------------------------------------------------------------')

    # Imprime el nombre del proyecto y el gerente del proyecto 01
    # my_project_manager_02.print_project()

    # Asignando los programadores al equipo del Proyecto / Gerente de Proyecto
    my_project_manager_02.add_team_member(my_programmer_05)
    my_project_manager_02.add_team_member(my_programmer_06)
    my_project_manager_02.add_team_member(my_programmer_07)
    my_project_manager_02.add_team_member(my_programmer_08)
   
    # Imprime el equipo del Proyecto (Los programadores asignados al Gerente del proyecto)
    # my_project_manager_02.print_team()

    # Asignando tareas a los programadores desde el Gerente del Proyecto
    my_project_manager_02.assign_tasks(my_programmer_05, "Diseñar Base de Datos / Backend")
    my_project_manager_02.assign_tasks(my_programmer_06, "Implementar login / Middleware")
    my_project_manager_02.assign_tasks(my_programmer_07, "Diseñar Maquetado / Frontend")
    my_project_manager_02.assign_tasks(my_programmer_08, "Diseñar / Implementar API REST")
    #print('--------------------------------------------------------------------------')

    # Probando el sistema de commits de los programadores asignados al proyecto 01
    # my_programmer_01.commit("Login implemented")
    # my_programmer_02.commit("Registration implemented")
    # my_programmer_03.commit("Layout designed")
    # my_programmer_04.commit("Database designed")
    # print('--------------------------------------------------------------------------')

    # Probando el sistema de commits de los programadores asignados al proyecto 02
    # my_programmer_05.commit("Database designed / Backend implemented")
    # my_programmer_06.commit("Login implemented / Middleware implemented")
    # my_programmer_07.commit("Layout designed / Frontend implemented")
    # my_programmer_08.commit("API REST designed / implemented")


    while True:
        Menu()
        opc = int(input("Escoge una opcion: "))
        match opc:
            case 1:
                while True:
                    my_manager.menuManager()
                    opc1 = int(input("Escoge una opcion: "))
                    match opc1:
                        case 1:
                            print(f'Nota: \nExpense < COP50000 || Has Ticket: "n" => Auto Approved \nExpense > COP50000 || Has Ticket: "n" => Denied. \nExpense > COP50000 || Has Ticket: "s" => Approved.')   
                            monto = float(input("Digite el monto: "))
                            ticket_input: str = input("¿Cuenta con ticket? (s/n): ")
                            ticket: bool = ticket_input.lower() == 's' or ticket_input.lower() == 'si'
                            my_manager.approvals(monto, ticket)
                            x: str = input("Press <Enter> to continue...")
                        case 2:
                            my_manager.print_approvals()
                            x: str = input("Press <Enter> to continue...")
                        case 3:
                            my_manager.print_department()
                            my_manager.print_team()
                            x: str = input("Press <Enter> to continue...")
                        case 0:
                            break
            case 2:
                my_manager.print_team()
                project_manager_id: int = int(input('From team members list below, Write project manager id: '))
                for member_manager_team in my_manager.team:
                    if member_manager_team.id == project_manager_id:
                        my_project_manager: Employee = my_manager.select_member_team(member_manager_team)
                        break

                while True:
                    my_project_manager.menuProjectManager()
                    opc2 = int(input("Escoge una opcion: "))
                    match opc2:
                        case 1:
                            my_project_manager.print_project()
                            my_project_manager.print_team()
                            x: str = input("Press <Enter> to continue...")

                        case 2:
                            my_project_manager.print_team()
                            programmer_id: int = int(input('From team members list below, Write programmer id: '))
                            for member_project_manager_team in my_project_manager.team:
                                if member_project_manager_team.id == programmer_id:
                                    my_programmer: Employee = my_project_manager.select_member_team(member_project_manager_team)
                                    break

                            task_description: str = input("Ingrese la descripción de la tarea: ")
                            my_project_manager.assign_tasks(my_programmer, task_description)
                            x: str = input("Press <Enter> to continue...")

                        case 3:
                            # La solución es funcional pero voy a probar otra forma:
                            # for dev_task in my_project_manager.tasks.items():
                            #     print(f'Dev: {dev_task[0].name} | Task: "{dev_task[1]}"')
                            
                            for dev, task in my_project_manager.tasks.items():
                                print(f'Dev: {dev.name} | Task: "{task}"')

                            x: str = input("Press <Enter> to continue...")
   
                        case 0:
                            break

            case 3:
                print("Funcionalidad de desarrollo aún no implementada.")
                x = input("Press <Enter> to continue...")
            case 0:
                print("Saliendo del programa...")
                x: str = input("Press <Enter> to continue...")
                break


main()
