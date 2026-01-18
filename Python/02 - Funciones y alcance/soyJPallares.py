
# /*
#  * EJERCICIO:
#  * - Crea ejemplos de funciones básicas que representen las diferentes
#  *   posibilidades del lenguaje:
#  *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
#  * - Comprueba si puedes crear funciones dentro de funciones.
#  * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
#  * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
#  * - Debes hacer print por consola del resultado de todos los ejemplos.
#  *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
#  * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#  *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#  *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#  *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#  *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
#  *
#  * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
#  * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
#  */

"""
Funciones definidas por el usuario
"""

# Simple

def greet():
    print("Hola, Python!")

greet()

# Con retorno

def return_greet():
    return "Hola, Python!"

print(return_greet())

# Con un argumento

def arg_greet(name):
    print(f"Hola, {name}!")

arg_greet("Brais")

# Con argumentos

def args_greet(greet, name):
    print(f"{greet}, {name}!")

args_greet("Hi", "Brais")
args_greet(name="Brais", greet="Hi")

# Con un argumento predeterminado

def default_arg_greet(name="Python"):
    print(f"Hola, {name}!")

default_arg_greet("Brais")
default_arg_greet()

# Con argumentos y return

def return_args_greet(greet, name):
    return f"{greet}, {name}!"

print(return_args_greet("Hi", "Brais"))

# Con retorno de varios valores


def multiple_return_greet():
    return "Hola", "Python"

greet, name = multiple_return_greet()
print(greet)
print(name)

# Con un número variable de argumentos

def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}!")

variable_arg_greet("Python", "Brais", "MoureDev", "comunidad")

# Con un número variable de argumentos con palabra clave

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"{value} ({key})!")


variable_key_arg_greet(
    language="Python",
    name="Brais",
    alias="MoureDev",
    age=36
)

"""
Funciones dentro de funciones
"""

def outer_function():
    def inner_function():
        print("Función interna: Hola, Python !")
    inner_function()

outer_function()

"""
Funciones del lenguaje (built-in)
"""

print(len("MoureDev"))
print(type(36))
print("MoureDev".upper())

"""
Variables locales y globales
"""

global_var = "Python"

def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_var}!")

print(global_var)
# print(local_var) No se puede acceder desde fuera de la función

hello_python()

"""
Extra
"""

def print_numbers(text1, text2) -> int:
    count = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(text1 + text2)
        elif i % 3 == 0:
            print(text1)
        elif i % 5 == 0:
            print(text2)
        else:
            print(i)
            count += 1
    return count

print(print_numbers("Fizz", "Buzz"))