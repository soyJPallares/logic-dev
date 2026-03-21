'''
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 * ****************************************
 * 1. Palíndromos
 *   Son palabras o frases que se leen igual de izquierda a derecha que de derecha a izquierda. En el caso de las frases, 
 *   se ignoran los espacios y signos de puntuación. 
 *       Ejemplos de palabras: Oso, reconocer, seres.
 *       Ejemplos de frases: "Anita lava la tina", "Dábale arroz a la zorra el abad". 
 * 2. Anagramas
 *   Consisten en crear una palabra o frase nueva reordenando exactamente las mismas letras de otra palabra o frase original. 
 *       Ejemplos:
 *           Roma → Amor o Mora.
 *           Lácteo → Coleta.
 *           Frase → Fresa. 
 * 3. Isogramas
 *   Es una palabra en la que no se repite ninguna letra. 
 *   Si cada letra aparece exactamente el mismo número de veces (por ejemplo, todas aparecen dos veces), se denomina isograma de segundo orden. 
 *       Ejemplos: Centrifugado, Vislumbrar, Pueblo.
 '''
import os
import platform
#import time

def clscr():
    if platform.system() == "Windows": os.system("cls")
    else: os.system("clear")


def Menu():
    print("Menu")
    print("1. Palíndromos")
    print("2. Anagrama")
    print("3. Isograma")
    print("0. Salir")


def Palindromos (p1):
    p2 = p1
    p2 = list(p2)
    p2.reverse()
    p2 = "".join(p2)
    if p1.lower() == p2.lower():
        return print("La palabra es palindroma")
    else:
        return print("La palabra no es palindroma")
    

def Anagramas (p1, p2):
    
    p1 = p1.lower()
    p2 = p2.lower()

    p1 = list(p1)
    p2 = list(p2)
    p1.sort()
    p2.sort()
    p1 = "".join(p1)
    p2 = "".join(p2)
    if p1 == p2:
        print("Las palabras son anagramas")
    else:
        print("Las palabras no son anagramas")

def Isogramas (p1):
    p1 = p1.lower()
    for i in p1:
        if p1.count(i) > 1:
            return print("La palabra no es un isograma")
        else:
            return print("La palabra es un isograma")

while True:
    Menu()
    opc = int(input("Escoge una opcion: "))
    match opc:
        case 1:
            Palabra1 = input("Digite la palabra a comparar: ")
            #Palabra2 = input("Digite la segunda palabra a comparar: ")
            print(Palindromos(Palabra1))
        case 2:
            Palabra1 = input("Digite la palabra a comparar: ")
            Palabra2 = input("Digite la segunda palabra a comparar: ")
            print(Anagramas(Palabra1, Palabra2))
        case 3:
            Palabra1 = input("Digite la palabra a comparar: ")
            print(Isogramas(Palabra1))
        case 0:
            break
            clscr()
        case _:
            print("Opcion no valida")