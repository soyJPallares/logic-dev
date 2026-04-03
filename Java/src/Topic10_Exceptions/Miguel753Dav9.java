package Topic10_Exceptions;

public class Miguel753Dav9 {
    public static void main(String[] args) {
        try {
            int[] myNumbers = {1, 2, 3};
            System.out.println(myNumbers[10]);
        } catch (Exception e) {
            System.out.println("Se ha producido un error: " + e);
        }
    }
}
