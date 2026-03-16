
'''
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.

'''
import os
import platform

# ++------------------------------------------------------------++
# ||     función clrscr (Clear Screen): Limpia la pantalla.     ||
# ++------------------------------------------------------------++

def clrscr():
    if platform.system() == "Windows": os.system("cls")
    else: os.system("clear")


class Pila:

    def __init__(self):
        self.stack: list[str] = []

    def Stack_Menu(self):
        print("1. Add item");
        print("2. Delete item");
        print("3. List items");
        print("0. Return");

    def push(self, word: str):
        self.stack.append(word)

    def pop(self):
        self.stack.pop();

    def print(self):
        print(f"Size: {(len(self.stack))} | Stack: ");

        for item in reversed(self.stack):
            print(f"{item}")


class Cola:

    def __init__(self):
            self.queue: list[str] = []

    def Queue_Menu(self):
        print("1. Add item")
        print("2. Delete item")
        print("3. List items")
        print("0. Return")

    def add(self, word: str):
        self.queue.append(word);

    def pop(self):
        self.queue.pop(0);

    def print(self):
        print(f"Size: {(len(self.queue))}\nQueue: {self.queue}");

def Menu(): 
        print("1. Pilas")
        print("2. Colas")
        print("0. Salir")

def main_Q08():

        myStack = Pila()
        myQueue = Cola()
        flag: bool = True

        myStack.push("Miguel")
        myStack.push("Jonatan")
        myStack.push("Amada")
        myStack.push("Ainara")
        myStack.push("Elena")
        myStack.push("Barranquilla")
        myStack.push("Medellín")
        myStack.push("Cali")
        myStack.push("Bogotá DC")

        myQueue.add("Miguel")
        myQueue.add("Jonatan")
        myQueue.add("Amada")
        myQueue.add("Ainara")
        myQueue.add("Elena")
        myQueue.add("Barranquilla")
        myQueue.add("Medellín")
        myQueue.add("Cali")
        myQueue.add("Bogotá DC")


        while (flag):
            clrscr()
            Menu()

            opt = int(input("Choice an option: "))
            match opt:
                case 1:
                    flag_stack: bool = True
                    while (flag_stack):
                        clrscr()
                        myStack.Stack_Menu()

                        opt_stack = int(input("Choice an option: "))
                        match opt_stack:
                            case 1:
                                Word_stack: str = input("Write item: ")
                                myStack.push(Word_stack)
                            
                            case 2: myStack.pop()

                            case 3:
                                myStack.print()
                                pause: str = input("Press any key to continue...")

                            case 0: flag_stack = False

                case 2:
                    flag_queue: bool = True
                    while (flag_queue):
                        clrscr()
                        myQueue.Queue_Menu()
                        
                        opt_queue: int = int(input("Choice an option: "))
                        match opt_queue:
                            case 1:
                                Word_queue: str = input("Write item: ")
                                myQueue.add(Word_queue)                            

                            case 2: myQueue.pop()

                            case 3: 
                                myQueue.print()
                                pause: str = input("Press any key to continue...")

                            case 0: flag_queue = False

                case 0: flag = False

main_Q08();
