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

file_name = "ventas_soyJPallares.txt"
# ----------------------------------------------------------------------------------
def crear_archivo() -> None:
# ----------------------------------------------------------------------------------
    with open(file_name, "w") as f:
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
def menu() -> None:
# ----------------------------------------------------------------------------------
    print("1. Añadir producto")
    print("2. Consultar productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Calcular venta total")
    print("6. Calcular venta por producto")
    print("7. Salir")

# ----------------------------------------------------------------------------------
def añadir () -> None:
# ----------------------------------------------------------------------------------
    print("Añadir producto")
    nombre = input("Nombre: ")
    cantidad = input("Cantidad: ")
    precio = input("Precio: ")

    with open(file_name, "a") as f:
        f.write(f"{nombre}, {cantidad}, {precio}.0\n")

# ----------------------------------------------------------------------------------
def consultar () -> None:
# ----------------------------------------------------------------------------------
    pass

# ----------------------------------------------------------------------------------
def actualizar () -> None:
# ----------------------------------------------------------------------------------
    pass

# ----------------------------------------------------------------------------------
def eliminar () -> None:
# ----------------------------------------------------------------------------------
    pass

# ----------------------------------------------------------------------------------
def ventaTotal () -> None:
# ----------------------------------------------------------------------------------
    pass

# ----------------------------------------------------------------------------------
def ventaPorProducto () -> None:
# ----------------------------------------------------------------------------------
    pass

# ----------------------------------------------------------------------------------
def main() -> None:
# ----------------------------------------------------------------------------------
    crear_archivo()

    with open(file_name) as f:
        print(f.read())

    # os.remove(file_name)

main()
