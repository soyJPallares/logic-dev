"""
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado.
 """
x = 10
def prueba_de_errores(a : str) -> str:
    if not isinstance(a, str):
        print(type(x))
        raise TypeError("ytujrj6hyuetuy")
    
try:
    prueba_de_errores(x)

except NameError as e:
    print(f"Tipo de error: {e}")
except ZeroDivisionError as e:
    print(f"Tipo de error: {e}")
except TypeError as e:
    print(f"Tipo de error: {e}")
else:
    print("No hay ningun error")
finally:
    print("Se ha terminado la prueba de errores")