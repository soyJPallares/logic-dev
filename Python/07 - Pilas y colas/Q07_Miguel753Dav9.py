"""
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 """

web = []
web.append("www.google.com")
web.append("www.yahoo.com")
web.append("www.reddit.com")
web.append("www.steam.com")
web.append("www.discord.com")

def browser():
    if len(web) == 1:
        print("No hay URL anterior")
    elif len(web) > 1:
        print(web[len(web) - 2])
        web.pop()
    else:
        print("La lista esta vacia")
    

while True:
    opc = input("")
    opc.lower()
    match opc:
        case "forward":
            print("Proximamente")
        case "back":
            browser()
        case "salir":
            break
        case _:
            web.append(opc)
            print("URL agregada")

print(web)

documents = []
documents.append("Los ojos de plata")
documents.append("The Twisted One")
documents.append("El cuarto armario")

def printer():
    if len(documents) < 1:
        print("No hay documentos en la cola ")
    else:
        print(documents[0])
        documents.pop(0)

while True:
    opc = input("")
    opc.lower()
    match opc:
        case "print":
            printer()
        case "salir":
            break
        case _:
            documents.append(opc)
            print("Documento agregado")