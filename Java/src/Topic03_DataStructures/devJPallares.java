package Topic03_DataStructures;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.HashMap;
import java.util.List;

public class devJPallares {
    public static void main(String[] args){

        // Listas [-] (Lista mutable de valores) - Indexada - Ordenable

        List<String> cars = new ArrayList<>();
        cars.add("Volvo");
        cars.add("BMW");
        cars.add("Ford");
        cars.add("Mazda");
        System.out.println(cars);

        // "List.of" crea una lista inmutable, permite definir los elementos de la lista al tiempo de crearla
        // Los elementos no se pueden cambiar, no se pueden agregar nuevos ni eliminar elementos existentes
        List<String> cities = List.of("Barranquilla", "Medellín","Cali", "Bogotá DC");
        System.out.println(cities);

        // En este ejemplo el objeto lista se crea con la keyword "new" por lo que es mutable
        // Podemos usar "List.of" dentro del constructor de la lista para definir los elementos de la lista
        // al tiempo de crearla
        List<String> countries = new ArrayList<>(List.of("Colombia", "Venezuela", "Perú", "Ecuador"));
        System.out.println(countries);

        // Sets [Sets en Python] (Lista de Valores) - Hasheable - Desordenada

        HashSet<String> names = new HashSet<>();
        names.add("Miguel");
        names.add("Jonatan");
        names.add("Amada");
        names.add("Ainara");
        names.add("Jonatan");
        names.add("Amada");
        names.add("Jonatan");
        System.out.println(names);

        // Mapas [Diccionarios en Python] (Pares Clave : Valor) - Hasheable - Desordenada

        HashMap<String, String> myMap = new HashMap<>();
        myMap.put("name", "Miguel");
        myMap.put("surname", "Pallares");
        myMap.put("alias", "Char");
        myMap.put("age", "11");
        System.out.println(myMap);

    }
}
