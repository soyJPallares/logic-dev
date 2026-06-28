import os
"""
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
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 """

"""
file_name = "Miguel753Dav9.txt"

with open (file_name, "w") as file:
    file.write("Hola mundo")

with open (file_name, "r") as file:
    print(file.read())
 """

file_name = "Miguel753Dav9_Q11.txt"
file_temp = "Temporal.txt"
def Menu():
    print("1. Añadir")
    print("2. Consultar")
    print("3. Actualizar")
    print("4. Eliminar productos")
    print("5. Calcular la venta total")
    print("6. Calcular la venta por producto")
    print("0. Salir")

while True:
    Menu()
    opc = int(input("Escoge una opcion: "))
    match opc:
        case 1:
            product = input("Ingrese el nombre del producto: ")
            quantity_sold = input("Ingrese la cantidad vendida: ")
            price = input("Ingrese el precio del producto: ")
            with open(file_name, "a") as file:
                file.write(product + ",")
                file.write(quantity_sold + ",")
                file.write(price + "\n")
        case 2:
            consulta = input("Producto a consultar: ")
            with open(file_name) as f:
                for x in f:
                    if consulta in x:
                        print(x)
        case 3:
            consulta2 = input("Producto a actualizar: ")
            new_quantity_sold = input("Digite la nueva cantidad vendida: ")
            new_price = input("Digite el nuevo precio: ")
            with open(file_name, "r+") as f:
                while True:
                    posicion_linea = f.tell()
                    linea = f.readline()

                    if not linea:
                        break

                    if consulta2 in linea:
                        f.seek(posicion_linea)
                        f.write(consulta2 + "," + new_quantity_sold + "," + new_price + "\n")
        case 4:
            consulta3 = input("Digite el producto a eliminar: ")
            with open(file_name, "r") as f_org, \
                open(file_temp, "w") as f_temp:

                for linea in f_org:
                    if consulta3 not in linea:
                        f_temp.write(linea)
            os.replace(file_temp, file_name)
        case 5:
            total = 0
            with open(file_name, "r") as f:
                for x in f:
                    partes = x.strip().split(",")

                    if len(partes) == 3:
                        product = partes[0]
                        quantity = int(partes[1])
                        price = int(partes[2])

                    subtotal = quantity * price
                    total += subtotal
            print(f"Ventas totales: {total}")
        case 6:
            print()
        case 0:
            #os.remove(file_name)
            break