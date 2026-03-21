"""
Operadores
"""
s1 = "Agua"
s2 = "Regulus"

# Concatenacion
print(s1 + ", " + s2 + "!")

# Repeticion
print(s1 * 3)

# Indexacion
print(s1[0] + s1[1] + s1[2] + s1[3])

# Longitud
print(len(s2))

# Slicing(porcion)
print(s2[2:7])
print(s2[2:]) # Va del 2 hasta el final
print(s2[0:2])
print(s2[:2]) # Va desde el prinicipio hasta el 2

# Busqueda
print("a" in s1)
print("ulu" in s2)

# Reemplazo
print(s2.replace("u", "a"))

# Mayúsculas, minúsculas y letras en mayúsculas
print(s1.upper())
print(s1.lower())
print("miguel david".title())
print("miguel david".capitalize())

# Eliminacion de espacios al principio y al final
print("||" + " miguel david ".strip() + "@migueldavid")

# Busqueda al principio y al final
print(s2.startswith("Re"))
print(s2.startswith("Ag"))
print(s2.endswith("gulus"))
print(s2.endswith("ua"))

s3 = "Miguel David @migueldavid"

# Busqueda de posicion
print("Miguel David @migueldavid".find("miguel"))
print("Miguel David @migueldavid".find("Miguel"))
print("Miguel David @migueldavid".find("M"))
print("Miguel David @migueldavid".lower().find("M"))

# Busqueda de ocurrencias
print(s3.lower().count("m"))

# Formateo
print("Saludo: {}, lenguaje{}!".format(s1, s2))

# Interpolación
print(f"Saludo: {s1}, lenguaje{s2}!")

# Transformacion de lista de caracteres
print(list(s3))

# Transformacion de lista en cadena
l1 = [s1, ", ", s2, "!"]
print("".join(l1))

# Transformaciones numericas
s4 = "123456"
s4 = int(s4)
print(s4)

s5 = "123456.123"
s5 = float(s5)
print(s5)

#Comprobaciones varias
s4 = "123456"
print(s1.isalnum())
print(s1.isalpha())
print(s4.isalpha())
print(s4.isnumeric())