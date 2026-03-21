"""
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 *
 *
 * La Sucesión de Fibonacci es una secuencia infinita de números naturales donde cada término (a partir del tercero) es la suma de los dos anteriores, comenzando usualmente por 0 y 1 (0, 1, 1, 2, 3, 5, 8, 13, ...), y aparece sorprendentemente en la naturaleza, el arte, la arquitectura y la computación, conectada estrechamente con la proporción áurea (Φ). Cómo se forma: Se empieza con los números 0 y 1.Cada número siguiente es la suma de los dos números previos.(0+1=1)(1+1=2)(1+2=3)(2+3=5)Y así sucesivamente: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ....
 *
"""

def Menu():
    print("Menu")
    print("1. Factorial")
    print("2. Sucesion de Fibonacci")
    print("0. Salir")

def factorial(number: int) -> int:
    if number < 0:
        print("Los números negativos no son válidos")
        return 0
    elif number == 0:
        return 1
    else:
        return number * factorial(number -1)


def fibonacci(posicion: int) -> int:
    if posicion < 1:
        print("No se puede poner una posicion negativa")
    elif posicion == 1:
        return 0
    elif posicion == 2:
        return 1
    else:
        return fibonacci(posicion -1) + fibonacci(posicion -2)
    
# a + b = c
# c + b = d
while True:
    Menu()
    opc = int(input("Elige una opcion: "))
    match opc:
        case 1:
            numero = int(input("Digite el numero a calcular: "))
            print(factorial(numero))
        case 2:
            numero = int(input("Digite la posicion de Fibonacci a consultar: "))
            print(fibonacci(numero))
        case 0:
            break
        case _:
            print("Opcion no valida")
