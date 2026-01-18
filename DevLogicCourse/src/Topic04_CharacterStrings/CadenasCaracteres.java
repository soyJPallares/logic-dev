package Topic04_CharacterStrings;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class CadenasCaracteres {
    public static void main(String[] args) {
        /*
        Operadores
         */
        String s1 = "Agua";
        String s2 = "Regulus";
        String s4 = " miguel pallares ";
        // Concatenacion
        System.out.println(s1 + " " + s2);
        // Repeticion
        String repetido = s1.repeat(3);
        // Indexacion
        char index0S1 = s1.charAt(0);
        char index3S1 = s1.charAt(3);
        // Longitud
        System.out.println(s1.length());
        // Slicing(porcion)
        String porcionS2 = s2.substring(2,7);
        System.out.println(porcionS2);
        // Busqueda
        System.out.println(s1.contains("a"));
        System.out.println(s2.contains("ulus"));
        // Reemplazo
        String s3 = s2.replace("u", "a");
        System.out.println(s3);
        // Mayúsculas, minúsculas y letras en mayúsculas
        System.out.println(s2.toUpperCase());
        System.out.println(s2.toLowerCase());
        System.out.println(capitalize("hola java"));
        System.out.println(title("hola java"));
        //Eliminacion de espacios al principio y al final
        System.out.println(s4);
        System.out.println(s4.trim());
        //Busqueda al principio y al final
        System.out.println(s2.startsWith("Re"));
        System.out.println(s2.startsWith("lus"));
        System.out.println(s2.endsWith("lus"));
        System.out.println(s2.endsWith("Re"));
        //Busqueda de posicion
        System.out.println(s2.indexOf("Re"));
        System.out.println(s2.indexOf("gulus"));
        System.out.println(s2.indexOf("r"));
        //Busqueda de ocurrencias
        count();
        //Formateo
        System.out.printf("Saludo: %s, lenguaje: %s\n", s1, s2);
        //Transformacion en lista de caracteres
        conver_List();
        //Transformacion de lista en cadena
        ArrayList<String> l1 = new ArrayList<>();
        l1.add(s1);
        l1.add(", ");
        l1.add(s2);
        l1.add("!");
        System.out.println(l1);
        String l2 = String.join("",l1);
        System.out.println(l2);

    }
    public static String capitalize(String texto) {
        if (texto == null || texto.isEmpty()) {
            return texto;
        }
        // Primera letra a Mayúscula + resto de la cadena
        return texto.substring(0, 1).toUpperCase() + texto.substring(1).toLowerCase();
    }
    public static String title(String texto) {
        if (texto == null || texto.isEmpty()) return texto;

        StringBuilder resultado = new StringBuilder();
        boolean proximaMayuscula = true;

        for (char c : texto.toCharArray()) {
            if (Character.isSpaceChar(c)) {
                proximaMayuscula = true;
                resultado.append(c);
            } else if (proximaMayuscula) {
                resultado.append(Character.toUpperCase(c));
                proximaMayuscula = false;
            } else {
                resultado.append(Character.toLowerCase(c));
            }
        }
        return resultado.toString();
    }
    static void count(){
        String s2 = "Regulus";
        String buscar = "u";
        int contador = 0;
        int indice = 0;

        while ((indice = s2.indexOf(buscar, indice)) != -1) {
            contador++;
            indice += buscar.length(); // Saltamos la palabra encontrada
        }

        System.out.println("Repeticiones: " + contador);
    }
    static void conver_List(){
        String s2 = "Regulus, Harry, Hermione, Ronald";
        List<String> listaS2 = new ArrayList<>(Arrays.asList(s2.split(",")));

        System.out.println(s2);
        System.out.println(listaS2);
    }
}