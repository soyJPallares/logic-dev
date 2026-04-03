'''
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
 '''

x = 10
y: list[int] = [1, 2, 3, 4]

def excepciones(x: int, y: list[int]) -> str:
    
    if not isinstance(x, int):
        raise TypeError(f"The first Parameter: x=(\"{x}\"), must be an integer")
    elif not isinstance(y, list) or not all(isinstance(i, int) for i in y):
        raise TypeError(f"The second Parameter: y=(\"{y}\"), must be contain a list of integers")
    else:
        print(f'Divividendo: {x}')
        print(f'Divisores: {y}\n{"-"*10}')
        for i in y:
            print(f'{x} / {i} = {x/i:.1f}')
    
try:
    excepciones(x, y)

except NameError as e:
    print(f'Error type: "{e}" [The variable "{e.name}" is not defined]')
except ZeroDivisionError as e:
    print(f'Error type: "{e}" [You can\'t divide by zero]')
except TypeError as e:
    print(f'Error type: "{e}" [The data type of the any parameter: \n(x: "{type(x)}", y: "{type(y)}" or list contained values in "{y}" isn\'t integer]')
else:
    print('Completed without exceptions')
finally:
    print('Exceptions testing finished')
