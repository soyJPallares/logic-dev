import java.util.Scanner;
/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la
 *   sucesión de Fibonacci (la función recibe la posición).
 *
 *
 * La Sucesión de Fibonacci es una secuencia infinita de números naturales donde cada término (a partir del tercero) es la suma de los dos anteriores, comenzando usualmente por 0 y 1 (0, 1, 1, 2, 3, 5, 8, 13, ...), y aparece sorprendentemente en la naturaleza, el arte, la arquitectura y la computación, conectada estrechamente con la proporción áurea (Φ). Cómo se forma: Se empieza con los números 0 y 1.Cada número siguiente es la suma de los dos números previos.(0+1=1)(1+1=2)(1+2=3)(2+3=5)Y así sucesivamente: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ....
 *
 */
public class Q06 {
    public static void main(String[] args){
        boolean flag = true;
        while (flag) {
            Menu();
            Scanner capOption = new Scanner(System.in);
            System.out.print("Escoga la opcion: ");
            int opc = capOption.nextInt();
            switch (opc) {
                case 1 :
                        Scanner capNumber = new Scanner(System.in);
                        System.out.print("Digite el numero a calcular: ");
                        int number = capNumber.nextInt();
                        System.out.println(Factorial(number));
                        break;
                case 2 :
                        Scanner capNumber2 = new Scanner(System.in);
                        System.out.print("Digite la posicion de Fibonacci a consultar: ");
                        int number2 = capNumber2.nextInt();
                        System.out.println(Fibonacci(number2));
                        break;
                case 0:
                    flag = false;
                default:
                        System.out.println("Opcion no valida");
            }
        }
    }
    static void Menu(){
        System.out.println("Menu");
        System.out.println("1. Factorial");
        System.out.println("2. Sucesion de Fibonacci");
        System.out.println("0. Salir");
    }
    static int Factorial(int number){
        if (number < 0){
            System.out.println("Los números negativos no son válidos");
            return 0;
        } else if (number == 0) {
            return 1;
        }
        else {
            return number * Factorial(number - 1);
        }
    }
    static int Fibonacci(int number){
        if (number < 1){
            System.out.println("No se puede poner una posicion negativa");
        } else if (number == 1) {
            return 0;
        } else if (number == 2) {
            return 1;
        }
        else {
            return Fibonacci(number - 1) + Fibonacci(number - 2);
        }
        return 0;
    }
}
