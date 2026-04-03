'''
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 '''
# ------------------------------------------------------------------------------------------
'''Ejemplo metodo isintance(myObj, type) -> bool y all(dataEstructure, condition) -> bool'''
# ------------------------------------------------------------------------------------------
# x = isinstance("Hello", (str, float, int, str, list, dict, tuple))
# y: list[int] = [1, 2, 3, '']
# z = isinstance(y, list)

# print(x)
# print(z)

# #print('\n')
# r = all(isinstance(i, int) for i in y)
# print(r)

# #print('\n')
# for i in y:
# 	print(isinstance(i, int))

x: int = 10
y: list[int] = [1,2,3,0]

try:
    
    print(xy
    for i in y:
         print(f'{x/i:.1f}')

    # print(x[4])
      
except Exception as e:
    print(f"Se ha producido un error: {e}")