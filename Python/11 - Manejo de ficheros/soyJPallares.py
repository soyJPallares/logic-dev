''' 
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
'''
import os

file_name = "soyJPallares.txt"

with open(file_name, "w") as file:
    file.write("Jonatan Pallares\n")
    file.write("48\n")
    file.write("Python")

with open(file_name, "r") as file: # with open(file_name) as file:
    print(file.read())

# os.remove(file_name)