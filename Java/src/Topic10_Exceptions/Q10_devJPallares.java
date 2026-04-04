
// * DIFICULTAD EXTRA (opcional):
// * Crea una función que sea capaz de procesar parámetros, pero que también
// * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
// * corresponderse con un tipo de excepción creada por nosotros de manera
// * personalizada, y debe ser lanzada de manera manual) en caso de error.
// * - Captura todas las excepciones desde el lugar donde llamas a la función.
// * - Imprime el tipo de error.
// * - Imprime si no se ha producido ningún error.
// * - Imprime que la ejecución ha finalizado.

package Topic10_Exceptions;

import java.awt.*;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Q10_devJPallares {

    static Integer capt_dividendo () {
        Scanner capDiv = new Scanner(System.in);

        System.out.print("Digite el dividendo: ");
        String a = capDiv.nextLine(); // Leer como texto primero

        try {
            return Integer.parseInt(a); // Intentar convertir
        } catch (NumberFormatException e) {
            throw new InputMismatchException("The Parameter must be an integer");
        }
    }

    static void exceptions(Integer b, int[] c) {

        for (int i : c) {
            if (i == 0) {
                throw new ArithmeticException("Can't divide by zero");
            } else {
                System.out.printf("%d // %d = %d\n", b, i, b / i);
            }
        }
        System.out.println("------------------------------------------");
    }

    public static void main(String[] args) {
        int[] y = {1, 2, 3, 4};

        try {
            int x = capt_dividendo();
            System.out.println("------------------------------------------");
            System.out.printf("Dividendo: %d\n", x);
            System.out.printf("Divisores: ");
            for (int j : y) {
                System.out.printf("[%d]", j);
            }
            System.out.printf("\n------------------------------------------\n");

            exceptions(x,y);

        } catch (ArithmeticException e) {
            System.out.printf("Error: \n%s", e);
        } catch (InputMismatchException e) {
            System.out.printf("Error: \n%s", e);
        } catch (Exception e) {
            System.out.printf("Error: \n%s", e);
        } finally {
            System.out.printf("\nSe completó la ejecución del programa");
        }
    }
}
