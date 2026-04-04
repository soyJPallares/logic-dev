
// * EJERCICIO:
// * Explora el concepto de manejo de excepciones según tu lenguaje.
// * Fuerza un error en tu código, captura el error, imprime dicho error
// * y evita que el programa se detenga de manera inesperada.
// * Prueba a dividir "10/0" o acceder a un índice no existente
// * de un listado para intentar provocar un error.

package Topic10_Exceptions;

public class soyJPallares {
    public static void main(String[] args) {

        Integer x = 10;
        int[] y = {1, 2, 3, 0};

        System.out.printf("Dividendo: %d", x);
        System.out.printf("Divisores: ");
        for (int j : y) {
            System.out.printf("[%d]", j);
        }
        System.out.println();

        try {
            //System.out.println(y[4]);
            for (int i : y) {
                System.out.printf("%d // %d = %d\n", x, i, x/i);
            }
        } catch (Exception e) {
            System.out.printf("Se ha producido un error: \n%s", e);
        } finally {
            System.out.printf("\nSe completó la ejecución del programa");
        }
    }
}
