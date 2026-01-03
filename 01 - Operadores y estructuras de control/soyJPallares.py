
# /*
#  * EJERCICIO:
#  * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#  *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#  *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
#  * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#  *   que representen todos los tipos de estructuras de control que existan
#  *   en tu lenguaje:
#  *   Condicionales, iterativas, excepciones...
#  * - Debes hacer print por consola del resultado de todos los ejemplos.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que imprima por consola todos los números comprendidos
#  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
#  *
#  * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
#  */

#-----------
# Operadores
#-----------

# Operadores aritméticos

print(f"Suma: 10 + 3 = {10 + 3}")               # 13
print(f"Resta: 10 - 3 = {10 - 3}")              # 7
print(f"Multiplicación: 10 * 3 = {10 * 3}")     # 30
print(f"División: 10 / 3 = {10 / 3}")           # 3.3333333333
print(f"Módulo: 10 % 3 = {10 % 3}")             # 1
print(f"Exponente: 10 ** 3 = {10 ** 3}")        # 1000
print(f"División entera: 10 // 3 = {10 // 3}")  # 3

# Operadores de comparación

print(f"Igualdad: 10 == 3 es {10 == 3}")            # False
print(f"Desigualdad: 10 != 3 es {10 != 3}")         # True
print(f"Mayor que: 10 > 3 es {10 > 3}")             # True
print(f"Menor que: 10 < 3 es {10 < 3}")             # False
print(f"Mayor o igual que: 10 >= 10 es {10 >= 10}") # True
print(f"Menor o igual que: 10 <= 3 es {10 <= 3}")   # False

# Operadores lógicos

print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")  # True
print(f"OR ||: 10 + 3 == 14 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}")     # True
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}")                         # True

# Operadores de asignación

my_number = 11      # asignación
print(my_number)    # 11
my_number += 1      # suma y asignación (SImplifica my_number = my_number + 1)
print(my_number)    # 12
my_number -= 1      # resta y asignación (SImplifica my_number = my_number - 1)
print(my_number)    # 11
my_number *= 2      # multiplicación y asignación (SImplifica my_number = my_number * 2)
print(my_number)    # 22
my_number /= 2      # división y asignación (SImplifica my_number = my_number / 2)
print(my_number)    # 11.0
my_number %= 2      # módulo y asignación (SImplifica my_number = my_number % 2)
print(my_number)    # 1.0
my_number **= 1     # exponente y asignación (SImplifica my_number = my_number ** 1)
print(my_number)    # 1.0
my_number //= 1     # división entera y asignación (SImplifica my_number = my_number // 1)
print(my_number)    # 1.0

# Operadores de identidad ("Is" Compara las posiciones en la memoria, no los valores)

my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")        # True
print(f"my_number is not my_new_number es {my_number is not my_new_number}")# False

# Operadores de pertenencia

print(f"'u' in 'mouredev' = {'u' in 'mouredev'}")           # True
print(f"'b' not in 'mouredev' = {'b' not in 'mouredev'}")   # True

# Operadores de bit (Comparan los valores binarios bit a bit)

a = 10  # 1010
b = 3   # 0011
print(f"AND: 10 & 3 = {10 & 3}")    # 0010 ('1' si ambos son '1', '0' si alguno es '0')
print(f"OR: 10 | 3 = {10 | 3}")     # 1011 ('0' si ambos son '0', '1' si alguno es '1')
print(f"XOR: 10 ^ 3 = {10 ^ 3}")    # 1001 ('0' si son iguales, '1' si son diferentes)
print(f"NOT: ~10 = {~10}")          # 0101 (Invierte todos los bits) 
                                    # (La operación '~n' es equivalente a '-(n + 1)' en decimal)
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")  # 0010
                                                            # '>>' Mueve los bits del número hacia la derecha 
                                                            # el número de posiciones especificado. 
                                                            # Los bits que "se caen" por la derecha se pierden, 
                                                            # y se insertan 0's por la izquierda.
'''
    * Ejemplo: 10 >> 2 (Desplazar '1010' dos posiciones a la derecha)
        1. Original: 1010
        2. Desplazar una vez: 0101
        3. Desplazar dos veces: 0010
    El binario '0010' es 2 en decimal.

    Matemáticamente: Desplazar a la derecha n posiciones 
    es equivalente a realizar una 'división entera' por 2^n (ignorando el signo).
    10 >> 2 ==> (10 // 2^2) = (10 // 4) = 2
'''

print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")  # 101000
                                                            # '<<' Mueve los bits del número hacia la izquierda 
                                                            # el número de posiciones especificado. 
                                                            # Se insertan 0's por la derecha.
'''
    * Ejemplo: 10 << 2 (Desplazar '1010' dos posiciones a la izquierda)
        1. Original: 1010
        2. Desplazar una vez: 10100
        3. Desplazar dos veces: 101000
    El binario '101000' es 40 en decimal (32 + 8 = 40).

    Matemáticamente: Desplazar a la izquierda n posiciones 
    es equivalente a realizar una multiplicación por 2^n.
    10 << 2 ==> (10 X 2^2) = (10 X 4) = 40
'''

#-----------------------
# Estructuras de control
#-----------------------

# Condicionales

my_string = "Jonatan"

if my_string == "soyJPallares":
    print("my_string es 'soyJPallares'")
elif my_string == "Jonatan":
    print("my_string es 'Jonatan'")
else:
    print("my_string no es 'soyJPallares' ni 'Jonatan'")

# Iterativas

for i in range(11):
    print(i)

i = 0
while i <= 10:
    print(i)
    i += 1

# Manejo de excepciones

try:
    print(10 / 0)
except ZeroDivisionError:
    print("La división por cero no está definida")
finally:
    print("Ha finalizado el manejo de excepciones")

#------
# Extra
#------

for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)