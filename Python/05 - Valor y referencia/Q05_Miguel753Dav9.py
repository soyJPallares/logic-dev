"""
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
"""
value1 = "Sirius"
value2 = "Black"

reference1 = ["Bilbo"]
reference2 = ["Bolson"]

def value (v1, v2):
    v3 = v1

    v1 = v2
    v2 = v3
    return v1, v2

def reference (r1, r2):
    r3 = r1

    r1 = r2
    r2 = r3
    return r1, r2

x, y = value(value1, value2)
print(value1)
print(value2)
print(x)
print(y)

a, b = reference(reference1, reference2)
print(reference1)
print(reference2)
print(a)
print(b)