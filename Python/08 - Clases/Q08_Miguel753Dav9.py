"""
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
"""
def Menu():
    print("1. Pilas")
    print("2. Colas")
    print("0. Salir")

stack = ["Espada", "Pollo frito", "Lanzacohetes", "Resortera"]
class Stack:

    def Menu():
        print("1. Añadir elemento")
        print("2. Eliminar elemento")
        print("3. Imprimir los elementos")
        print("0. Regresar")
    
    def push(word):
        stack.append(word)
    
    def pop():
        stack.pop()

    def print():
        print(len(stack))
        print(stack)
    
    def __init__(self):
        pass

queque = ["Espada", "Pollo frito", "Lanzacohetes", "Resortera"]
class Queque:
    def Menu():
        print("1. Añadir elemento")
        print("2. Eliminar elemento")
        print("3. Imprimir los elementos")
        print("0. Regresar")

    def push(word):
        queque.append(word)
    
    def pop():
        queque.pop(0)

    def print():
        print(len(queque))
        print(queque)
    
    def __init__(self):
        pass

while True:
    Menu()
    opc = int(input("Elige una opcion: "))
    match opc:
        case 1:
            while True:
                Stack.Menu()
                option = int(input("Elige una opcion: "))
                match option:
                    case 1:
                        word = input("Digite la palabra a introducir: ")
                        Stack.push(word)
                    case 2:
                        Stack.pop()
                    case 3:
                        Stack.print()
                    case 0:
                        break
                    case _:
                        print("Opcion no valida")
        case 2:
            while True:
                Queque.Menu()
                opt = int(input("Elige una opcion: "))
                match opt:
                    case 1:
                        word = input("Digite la palabra a introducir: ")
                        Queque.push(word)
                    case 2:
                        Queque.pop()
                    case 3:
                        Queque.print()
                    case 0:
                        break
                    case _:
                        print("Opcion no valida")
        case 0:
            break
        case _:
            print("Opcion no valida")