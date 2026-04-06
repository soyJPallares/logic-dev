''' 
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
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
'''

import os

file = "ventas_soyJPallares.txt"
# ----------------------------------------------------------------------------------
def crear_archivo() -> None:
# ----------------------------------------------------------------------------------
    
    if not os.path.exists(file):
        with open(file, "a") as f:
            f.write("Procesador AMD Ryzen 9, 15, 2450000.0\n")
            f.write("Procesador Intel Core i9, 12, 2410000.0\n")
            f.write("Tarjeta de Video NVIDIA RTX, 8, 6550000.0\n")
            f.write("Tarjeta de Video AMD Radeon, 10, 3890000.0\n")
            f.write("Memoria RAM Corsair DDR5, 45, 515000.0\n")
            f.write("Disco SSD Samsung NVMe, 30, 720000.0\n")
            f.write("Placa Base ASUS ROG, 7, 2050000.0\n")
            f.write("Fuente de Poder EVGA, 22, 550000.0\n")
            f.write("Gabinete NZXT, 14, 740000.0\n")
            f.write("Refrigeración Líquida Corsair, 18, 775000.0\n")
            f.write("Monitor LG UltraGear, 25, 1230000.0\n")
            f.write("Teclado Mecánico Logitech, 20, 940000.0\n")
            f.write("Mouse Razer DeathAdder, 35, 610000.0\n")
            f.write("Disco Duro Seagate, 12, 820000.0\n")
            f.write("Tarjeta de Sonido Creative, 5, 1430000.0\n")
            f.write("Mando Xbox Wireless, 50, 245000.0\n")
            f.write("Cámara Web Logitech, 40, 285000.0\n")
            f.write("Auriculares HyperX Cloud, 28, 405000.0\n")
            f.write("Pasta Térmica Thermal Grizzly, 100, 51000.0\n")
            f.write("Adaptador Wi-Fi TP-Link, 15, 185000.0\n")

# ----------------------------------------------------------------------------------
def add () -> None:
# ----------------------------------------------------------------------------------
    print(f"{'-'*21}\n|  Añadir producto  |\n{'-'*21}")
    nombre = input("Nombre del Producto: ")
    cantidad = input("Cantidad Vendida: ")
    precio = input("Precio Unitario: ")

    with open(file, "a") as f:
        f.write(f"{nombre}, {cantidad}, {precio}.0\n")

# ----------------------------------------------------------------------------------
def find () -> None:
# ----------------------------------------------------------------------------------
    print(f"{'-'*21}\n|  Buscar producto  |\n{'-'*21}")
    producto: str = input("Nombre del Producto: ")

    with open(file) as f:
        lines: list[str] = f.readlines()

    # Buscar la línea
    for line in lines:
        if producto in line:
            print(f"Producto encontrado: {line.strip()}")

# ----------------------------------------------------------------------------------
def update () -> None:
# ----------------------------------------------------------------------------------
        print(f"{'-'*25}\n|  Actualizar producto  |\n{'-'*25}")
        print(f"Nota: \nSe reemplaza solo una parte de la línea encontrada. \nSe reemplaza sólo la expresión literal exacta.")
        print(f"(Dejar vacío para no cambiar ningún valor)\n")
        producto: str = input("Nombre del Producto: ")

        with open(file) as f:
            lines: list[str] = f.readlines()

        # Buscar y editar la línea
        for i, line in enumerate(lines):
            if producto in line:
                print(f"Producto encontrado: {line.strip()}")                
                old_content: str = input("Contenido actual: ")
                new_content: str = input("Nuevo contenido: ")
                # Reemplazar línea completa
                # lines[i] = new_content.strip() + "\n"
                # Reemplazar solo una parte con el método replace (Sólo la palabra o expresión literal exacta):
                lines[i] = line.replace(old_content, new_content)

        # Reescribir el archivo
        with open(file, "w") as f:
            f.writelines(lines)

# ----------------------------------------------------------------------------------
def delete () -> None:
# ----------------------------------------------------------------------------------
        print(f"{'-'*21}\n|  Eliminar producto  |\n{'-'*21}")
        producto: str = input("Nombre del Producto: ")

        with open(file) as f:
            lines: list[str] = f.readlines()

        # Buscar y editar la línea
        for line in lines:
            if producto in line:
                print(f"Producto encontrado: {line.strip()} !!!")
                lines.remove(line)  # Eliminar la línea encontrada
                print(f"Producto eliminado!!!")

        # Reescribir el archivo
        with open(file, "w") as f:
            f.writelines(lines)


# ----------------------------------------------------------------------------------
def total_sales () -> None:
# ----------------------------------------------------------------------------------
    pass


# ----------------------------------------------------------------------------------
def product_sales () -> None:
# ----------------------------------------------------------------------------------
    pass


# ----------------------------------------------------------------------------------
def listing () -> None:
# ----------------------------------------------------------------------------------
    with open(file) as f:
        print(f.read())


# ----------------------------------------------------------------------------------
def menu() -> None:
# ----------------------------------------------------------------------------------
    print("1. Añadir producto")
    print("2. Consultar productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Listar productos")
    print("6. Calcular venta total")
    print("7. Calcular venta por producto")
    print("0. Salir")


# ----------------------------------------------------------------------------------
def main() -> None:
# ----------------------------------------------------------------------------------
    crear_archivo()
    # os.remove(file)
while True:
    menu()
    opc: str = input("Opción: ")
    print('')
    
    match opc:
        case '1': add()
        case '2': find()
        case '3': update()
        case '4': delete()
        case '5': listing()
        case '6': total_sales()
        case '7': product_sales()
        case '0': break
        case _: print('¡¡¡ Opción errada !!!')

main()
