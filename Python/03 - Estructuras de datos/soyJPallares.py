'''
Docstring for 03 - Estructuras de datos.soyJPallares

/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */
'''

"""
Estructuras
"""

# Listas

my_list: list = ["Jonatan", "Miguel", "Amada", "Elena"]
print(my_list)
my_list.append("MPallares")  # Inserción
my_list.append("JPallares")
print(my_list)
my_list.remove("Jonatan")  # Eliminación
print(my_list)
print(my_list[1])  # Acceso
my_list[1] = "Princesa"  # Actualización
print(my_list)
my_list.sort()  # Ordenación
print(my_list)
print(type(my_list))

# Tuplas

my_tuple: tuple = ("Brais", "Moure", "@mouredev", "36")
print(my_tuple[1])  # Acceso
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple))  # Ordenación
print(my_tuple)
print(type(my_tuple))

# Sets

my_set: set = {"Jonatan", "Pallares", "@devJPallares", "48"}
print(my_set)
my_set.add("devjpallares@gmail.com")  # Inserción
my_set.add("devjpallares@gmail.com")
print(my_set)
my_set.remove("Pallares")  # Eliminación
print(my_set)
my_set = set(sorted(my_set))  # No se puede ordenar
print(my_set)
#my_set.clear()
#print(my_set)

print(type(my_set))

# Diccionario

my_dict: dict = {
    "name": "Jonatan",
    "surname": "Pallares",
    "alias": "@soyJPallares",
    "age": "48"
}

print(my_dict)
my_dict["email"] = "arjonatanv@gmail.com"  # Inserción
print(my_dict)
del my_dict["surname"]  # Eliminación
print(my_dict)
print(my_dict["name"])  # Acceso
my_dict["age"] = "37"  # Actualización
print(my_dict)
my_dict = dict(sorted(my_dict.items()))  # Ordenación
print(my_dict)
print(type(my_dict))

