'''
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 '''

try:
    x: list[int] = [1,2,3,0]
    print(x)
    for i in x:
         print(f'{10/i:.1f}')

    # print(x[4])
      
except Exception as e:
    print(f"Se ha producido un error: {e}")