package Topic00_SintaxVariablesDataTypeAndHelloWorld;

public class HolaMundo {

    public static void main(String[] args){

        System.out.println("Hola, Java");

        //https://www.java.com/es/

        /*
        Este es un comentario
        de varias lineas
         */

        int n = 1; // Variable de tipo entero
        System.out.println("N: " + n);

        final float pi = 3.1416f; // Constante de tipo float (usa decimales)
        System.out.println("Pi: " + pi);

        int edad = 11; // Otra variable de tipo entero
        System.out.println("Edad: " + edad);

        String nombre = "Jonatan"; // Variable de tipo Cadena de caracteres
        System.out.printf("Nombre: %s\n", nombre);

        float estatura = 1.70f; // Variable de tipo float (usa decimales)
        System.out.printf("Estatura: %.2f\n", estatura);

        boolean mayor = false; // Variable de tipo Boolean (Usa logica booleana, Tiene dos valores posibles Verdadero o Falso)
        System.out.printf("Mayor:  %b\n", mayor);
    }
}
