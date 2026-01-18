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
 *   Son palabras o frases que se leen igual de izquierda a derecha que de derecha a izquierda. En el caso de las frases, se ignoran los espacios y signos de puntuación. 
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
import time


# ++------------------------------------------------------------++
# ||     función clrscr (Clear Screen): Limpia la pantalla.     ||
# ++------------------------------------------------------------++

def clrscr():
    if platform.system() == "Windows": os.system("cls")
    else: os.system("clear")

# ++-----------------------------------------------------------------------------------++
# ||     función Palíndromos: Evalua si una palabra es palindromo y retorna F o V.     ||
# ++-----------------------------------------------------------------------------------++

def func_palindromes (w1): 

    w2 = w1
    w2 = list(w2)
    
    w2.reverse()
    w2 = "".join(w2)
    
    if w1.lower() == w2.lower(): return True
    if w1.lower() != w2.lower(): return False


# ++------------------------------------------------------------------------------------------++
# ||     1. Palíndromos: Se leen igual de izquierda a derecha que de derecha a izquierda.     ||
# ++------------------------------------------------------------------------------------------++

def palindromes():
    clrscr()

    word = input("Digite la palabra a comprobar: ")

    if func_palindromes (word): return print("La palabra es palindroma")
    else: return print("La palabra no es palindroma")
    
# ++----------------------------------------------------------------------------------++
# ||     función Anagrama: Evalua si dos palabras son anagramas y retorna F o V.      ||
# ++----------------------------------------------------------------------------------++    

def func_anagrams (w1, w2):
    
    w1, w2 = w1.lower(), w2.lower()

    w1 = list(w1)
    w2 = list(w2)

    w1.sort(), w2.sort()
    w1, w2 = "".join(w1), "".join(w2) 

    if w1 == w2: return True
    if w1 != w2: return False


# ++-----------------------------------------------------------------------------------++
# ||     2. Anagrama: Palabra que contiene exactamente las mismas letras de otra.      ||
# ++-----------------------------------------------------------------------------------++    

def anagrams ():
    clrscr()
    
    word1 = input("Digite la primera palabra a comparar: ")
    word2 = input("Digite la segunda palabra a comparar: ")

    if func_anagrams(word1, word2): return print("Las palabras son anagramas")
    else: return print("Las palabras no son anagramas")


# ++----------------------------------------------------------------------------------++
# ||     función Isograma: Evalua si una palabra es un isograma y retorna F o V.      ||
# ++----------------------------------------------------------------------------------++  

def func_isogram(w1):

    for i in w1: # recorre la cadena un caracter a la vez
        if w1.lower().count(i) > 1: # La pone en minusculas y cuenta las coincidencias de cada caracter dentro de la cadena. 
            return False # Retorna False si cuenta mas de 1 coincidencia de cualquier caracter.
    return True # Retorna True si no encuentra mas de 1 coincidencia de ningún caracter.


# ++--------------------------------------------------++
# ||     3. Isograma: No se repite ninguna letra.     ||
# ++--------------------------------------------------++  

def isograms ():
    clrscr()

    word = input("Digite la palabra a comprobar: ")
    
    if func_isogram(word): return print("La palabra es un isograma")
    else: return print("La palabra NO es un isograma")


# ++--------------++
# ||     Menú     ||
# ++--------------++

def Menu():
    clrscr()
    print("Menu")
    print("1. Palíndromos") # Se leen igual de izquierda a derecha que de derecha a izquierda.
    print("2. Anagrama") # Palabra que contiene exactamente las mismas letras de otra. 
    print("3. Isograma") # No se repite ninguna letra.
    print("0. Salir")


# ++--------------++
# ||     Main     ||
# ++--------------++

def main():

    while True:

        Menu()
        opc = int(input("Escoge una opcion: "))
        print('')

        match opc:
            case 1:            
                palindromes()
                while True: # Ciclo While "infinito" para preguntar si se va a evaluar otro numero S/N
                    yes_not = input("Desea evaluar otra palabra [S/N]: ")
                    match yes_not.upper(): # .upper() Convierte y evalúa la opción en mayúscula
                        case 'S': palindromes() # Sólo "S" llama la función
                        case 'N': break # Sólo "N" rompe el ciclo While
                        case _: # Caso si presionas otra opción diferente a S ó N
                            print('¡¡¡ Opción errada !!!')
                            time.sleep(1.5) # Pausa breve para que el usuario lea el error
            case 2:
                anagrams()
                while True: # Ciclo While "infinito" para preguntar si se va a evaluar otro numero S/N
                    yes_not = input("Desea evaluar otro par de palabras [S/N]: ")
                    match yes_not.upper(): # .upper() Convierte y evalúa la opción en mayúscula
                        case 'S': anagrams() # Sólo "S" llama la función
                        case 'N': break # Sólo "N" rompe el ciclo While
                        case _: # Caso si presionas otra opción diferente a S ó N
                            print('¡¡¡ Opción errada !!!')
                            time.sleep(1.5) # Pausa breve para que el usuario lea el error
            case 3:
                isograms()
                while True: # Ciclo While "infinito" para preguntar si se va a evaluar otro numero S/N
                    yes_not = input("Desea evaluar otro par de palabras [S/N]: ")
                    match yes_not.upper(): # .upper() Convierte y evalúa la opción en mayúscula
                        case 'S': isograms() # Sólo "S" llama la función
                        case 'N': break # Sólo "N" rompe el ciclo While
                        case _: # Caso si presionas otra opción diferente a S ó N
                            print('¡¡¡ Opción errada !!!')
                            time.sleep(1.5) # Pausa breve para que el usuario lea el error
            case 0:
                break
            case _:
                print("Opcion no valida")

main()