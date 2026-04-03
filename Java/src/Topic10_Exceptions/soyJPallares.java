package Topic10_Exceptions;

import java.util.ArrayList;
import java.util.List;

public class soyJPallares {
    public static void main(String[] args) {
        Integer x = 10;
        List<Integer> y = new ArrayList<>(List.of(1, 2, 3, 4));

        try {
            System.out.println(x);
            System.out.println(y);
            //for
        } catch (Exception e) {
            //  Block of code to handle errors
        }
    }
}
