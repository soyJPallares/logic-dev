
#Operadores aritmeticos

print(f"Suma: 10 + 3 = {10 + 3}")
print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Multiplicacion: 10 * 3 = {10 * 3}")
print(f"Division: 10 / 3 = {10 / 3}")
print(f"Modulo: 10 % 3 = {10 % 3}")
print(f"Exponente: 10 ** 3 = {10 ** 3}")
print(f"Division entera: 10 // 3 = {10 // 3}")

#Operadores de comparacion

print(f"Igualdad: 10 == 3: {10 == 3}")
print(f"Desigual: 10 != 3: {10 != 3}")
print(f"Mayor que: 10 > 3: {10 > 3}")
print(f"Menor que: 10 < 3: {10 < 3}")
print(f"Mayor igual que: 10 >= 3: {10 >= 3}")
print(f"Menor igual que: 10 <= 10: {10 <= 10}")

#Operadores logicos
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 3}")
print(f"NOT !: not 10 + 3 == 13 es {not 10 + 3 == 14}")

#Operadores de asignacion
n = 11
print(n)
n += 1
print(n)
n -= 1
print(n)
n *= 2
print(n)
n /= 2
print(n)
n %= 2
print(n)
n **= 2
print(n)
n //= 2
print(n)

#Operadores de identidad
n = 32
new_n = n
print(n)
print(new_n)
print(f"n is new_n es {n is new_n}")
print(f"n is not new_n es {n is not new_n}")
print(f"{(2 + 3) * 4}")

#Operadores de pertenencia
print(f"u is moure{"u" is "moure"}")
print(f"u is not moure{"u" is not "moure"}")

#Operadores de bit
a = 10
b = 3
print(f"AND: 10 & 3 = {10 & 3}") # 0010
print(f"OR: 10 | 3 = {10 | 3}") # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") # 0010 
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}") # 101000

#Estructuras de datos

#Condicionales

my_string = "David"

if my_string == "Miguel":
    print("my_string es 'Miguel'")
elif my_string == "Pallares":
    print("my_string es 'Pallares'")
else:
    print("my_string no es ni 'Miguel' ni 'Pallares'")

#Iterativas

for i in range(11):
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1

#Manejo de excepciones

try:
    print(10 / 2)
except:
    print("Se ha generado un error")
finally:
    print("Ha finalizado el manejo de errores")