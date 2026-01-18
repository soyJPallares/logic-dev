package Topic04_CharacterStrings;

import java.util.Scanner;
import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.ListIterator;
import java.util.Collections;

/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 * *********************************************
 * 1. Palíndromos
 *   Son palabras o frases que se leen igual de izquierda a derecha que de derecha a izquierda. En el caso de las frases,
 *   se ignoran los espacios y signos de puntuación.
 *       Ejemplos de palabras: Oso, reconocer, seres.
 *       Ejemplos de frases: "Anita lava la tina", "Dábale arroz a la zorra el abad".
 * 2. Anagramas
 *   Consisten en crear una palabra o frase nueva reordenando exactamente las mismas letras de otra palabra o frase original.
 *       Ejemplos:
 *           Roma → Amor o Mora.
 *           Lácteo → Coleta.
 *           Frase → Fresa.
 * 3. Isogramas
 *   Es una palabra en la que no se repite ninguna letra.
 *   Si cada letra aparece exactamente el mismo número de veces (por ejemplo, todas aparecen dos veces), se denomina isograma de segundo orden.
 *       Ejemplos: Centrifugado, Vislumbrar, Pueblo.
 */

public class Q04 {
    public static void main(String[] args) {
        boolean flag = true;

        while (flag) {
            Menu();

            Scanner capOption = new Scanner(System.in);
            System.out.print("Escoja la opción: ");
            int opc = capOption.nextInt();

            switch (opc) {
                case 1 -> Palindromos();
                case 2 -> Anagramas();
                case 3 -> Isogramas();
                case 0 -> flag = false;
                default -> System.out.println("Opción no válida");
            }
        }
    }


//++--------------++
//||     Menú     ||
//++--------------++

    static void Menu() {

        System.out.printf("\nMenu\n");
        System.out.println("1. Palindromos");
        System.out.println("2. Anagramas");
        System.out.println("3. Isogramas");
        System.out.println("0. Salir");
    }


//++------------------------------------------------------------------------------------------++
//||     1. Palíndromos: Se leen igual de izquierda a derecha que de derecha a izquierda.     ||
//++------------------------------------------------------------------------------------------++

    static void Palindromos() {

        Scanner capWord = new Scanner(System.in);
        System.out.printf("\nDigite la palabra a comparar: ");
        String p1 = capWord.nextLine();

        List<String> listP2 = new ArrayList<>(Arrays.asList(p1.split("")));
        List<String> listP3 = new ArrayList<>(Arrays.asList());
        ListIterator<String> it = listP2.listIterator();

        while(it.hasNext()) {
            it.next();
        }
        while(it.hasPrevious()) {
            listP3.add(it.previous());
        }

        String p3 = String.join("",listP3);

        if (p1.toLowerCase().equals(p3.toLowerCase())){
            System.out.printf("\nla palabra %s es palindroma\n", p1);
        } else {
            System.out.printf("\nLa palabra %s NO es palindroma\n", p1);
        }
    }


//++-----------------------------------------------------------------------------------++
//||     2. Anagrama: Palabra que contiene exactamente las mismas letras de otra.      ||
//++-----------------------------------------------------------------------------------++

    static void Anagramas() {

        Scanner capWord = new Scanner(System.in);
        System.out.printf("\nDigite la palabra a comparar: ");
        String p1 = capWord.nextLine();
        System.out.printf("Digite la segunda palabra a comparar: ");
        String p2 = capWord.nextLine();

        p1 = p1.toLowerCase();
        p2 = p2.toLowerCase();

        List<String> listP1 = new ArrayList<>(Arrays.asList(p1.split("")));
        List<String> listP2 = new ArrayList<>(Arrays.asList(p2.split("")));

        listP1.sort(null);
        listP2.sort(null);

        String p3 = String.join("",listP1);
        String p4 = String.join("",listP2);

        if (p3.equals(p4)){
            System.out.printf("\nLas palabras %s y %s son un anagrama\n", p1, p2);
        } else {
            System.out.printf("\nLas palabras %s y %s NO son un anagrama\n", p1, p2);
        }
    }


//++--------------------------------------------------++
//||     3. Isograma: No se repite ninguna letra.     ||
//++--------------------------------------------------++

    static void Isogramas() {

        Scanner capWord = new Scanner(System.in);
        System.out.printf("\nDigite la palabra a comparar: ");
        String p1 = capWord.nextLine();

        String p2 = p1.toLowerCase();
        boolean esIsograma = true;
        List<String> listP1 = new ArrayList<>(Arrays.asList(p2.split("")));

        for (String i : listP1){
            if (Collections.frequency(listP1, i) > 1){
                esIsograma = false;
                break;
            }
        }

        if (esIsograma){
            System.out.printf("\nLa palabra %s es un isograma\n", p1);
        } else {
            System.out.printf("\nLa palabra %s NO es un isograma\n", p1);
        }
    }

}
