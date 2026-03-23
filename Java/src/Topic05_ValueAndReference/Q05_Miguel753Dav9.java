package Topic05_ValueAndReference;

import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

/*
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
 */

public class Q05_Miguel753Dav9 {
    public static void main(String[] args){
        String value1 = "Sirius";
        String value2 = "Black";

        ArrayList<String> reference1 = new ArrayList<String>();
        reference1.add("Bilbo");
        ArrayList<String> reference2 = new ArrayList<String>();
        reference2.add("Bolson");

        String[] values = value(value1, value2);
        String x = values[0];
        String y = values[1];
        System.out.println(value1);
        System.out.println(value2);
        System.out.println(x);
        System.out.println(y);

        ArrayList[] references = reference(reference1, reference2);
        ArrayList a = references[0];
        ArrayList b = references[1];
        System.out.println(reference1);
        System.out.println(reference2);
        System.out.println(a);
        System.out.println(b);

    }

    static String[] value (String v1, String v2){
        String v3 = v1;

        v1 = v2;
        v2 = v3;
        return new String[]{v1, v2};

    }
    static ArrayList[] reference (ArrayList r1, ArrayList r2){
        ArrayList r3 = r1;

        r1 = r2;
        r2 = r3;
        return new ArrayList[]{r1, r2};
    }

}
