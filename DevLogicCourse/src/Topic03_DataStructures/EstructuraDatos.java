package Topic03_DataStructures;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.HashMap;

public class EstructuraDatos {
    public static void main(String[] args){
        ArrayList<String> cars = new ArrayList<String>();
        cars.add("Volvo");
        cars.add("BMW");
        cars.add("Ford");
        cars.add("Mazda");
        System.out.println(cars);

        HashSet<String> names = new HashSet<String>();
        names.add("Miguel");
        names.add("Jonatan");
        names.add("Amada");
        names.add("Ainara");
        names.add("Jonatan");
        System.out.println(names);

        HashMap<String, String> myMap = new HashMap<String, String>();
        myMap.put("name", "Miguel");
        myMap.put("surname", "Pallares");
        myMap.put("alias", "Char");
        myMap.put("age", "11");
        System.out.println(myMap);

    }
}
