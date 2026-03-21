'''
Funciomes definidas por el usuario
'''

# Simple

def greet():
    print("Hola, Python")

greet()

# Con retorno

def return_greet():
    return "Hola, Python"

greet = return_greet()
print(return_greet())
print(greet)

# Con un argumento

def arg_greet(name):
    print(f"Hola, {name}")

arg_greet("Miguel")

# Con argumentos

def args_greet(greet, name):
    print(greet, name)

args_greet("Hola", "Python")

# Con un argumento predefinido

def default_arg_greet(name = "Python"):
    (print(f"Hola, {name}"))

default_arg_greet("Juanchito")
default_arg_greet()

#Funcion par e impar

def ParImpar(num):
    if num % 2 == 0: return True
    else: return False

print(ParImpar(2))

# Con retorno de varios valores

def mutiple_return_greet():
    return "Hola", "Python"

greet, name = mutiple_return_greet()
print(greet)
print(name)
print(mutiple_return_greet())

# Con un numero variable de argumentos

def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}!")

variable_arg_greet("Python", "Java", "Miguel", "Pallares")

# Con un numero variable de argumentos con palabras clave

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"{key}: {value}")

variable_key_arg_greet(
    language="Python", 
    name="Miguel", 
    alias="Char", 
    age=11
)

"""
Funciones dentro de funciones
"""

def outer_function():
    def inner_function():
        print("Funcion interna: Hola, Python")
    inner_function()

outer_function()

"""
Funciones del sistema (build-in)
"""
print(len("Miguel"))
print(type("Miguel"))
print("Miguel".upper)

"""
Variables locales y globales
"""

globalvar = "Python"

def hello_python():
    localvar = "Hola"
    print(f"{localvar},{globalvar}")

print(globalvar)

hello_python()

"""
Extra
"""

def numerbs1to100(text1, text2)-> int:
    contador = 0
    for i in range(1, 10):
        if i % 3 == 0 and i % 5 == 0:
            print(text1, text2)
            continue
        elif i % 3 == 0: 
            print(text1)
            continue
        elif i % 5 == 0: 
            print (text2)
            continue
        else:
            print(i) 
            contador += 1
    
    return contador
