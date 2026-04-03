package Topic10_Exceptions;

public class Q10_Miguel753Dav9 {
    static void prueba_de_errores (String a) {
        }
    public static void main(String[] args){
        Integer x = 10;
        System.out.println(x.getClass());
        try{
            Object animal = "Gato";
            Integer edad = (Integer) animal;
        }
        catch (ClassCastException e){
            System.out.println("Capturado: " + e.getMessage());
        }
    }
}
