package Topic02_FunctionsAndScope;

public class FuncionesAlcance {

    String globalvar = "Java";

    public static void main(String[] args){
        FuncionesAlcance myGlobalvar = new FuncionesAlcance();

        greet();
        System.out.println(return_greet());
        arg_greet("Miguel");
        args_greet("Hi ", "Miguel");
        default_name();
        System.out.println(ParImpar(2));
        outer_function();
        System.out.println(myGlobalvar.globalvar);
        hello_java();
    }
    // Simple
    static void greet(){
        System.out.println("Hola, Java");
    }
    // Con retorno
    static String return_greet(){
        return "Hola Java";
    }
    // Con un argumento

    static void arg_greet(String name){
        System.out.println("Hola " + name);
    }
    // Con argumentos
    static void args_greet(String greet, String name){
        System.out.println(greet + name);
    }
    // Con argumentos predefinidos

    static void default_name() {
        default_name("Java");
    }

    static void default_name(String name){
        System.out.println("Hola " + name);
    }

    //Funcion par e impar
    static boolean ParImpar(int num) {
        if (num % 2 == 0){return true;}
        else{return false;}
    }

    // Con retorno de varios valores || No existe, se trabaja con listas
    /*static String multiple_args_greet() {
        return "Hola", "Python"
    }*/
    //Funciones dentro de funciones
    static void outer_function(){
        class localClass {
            static void inner_function(){
                System.out.println("Funcion interna: Hola, Python");
            }
        }
        localClass myObj = new localClass();
        myObj.inner_function();
    }

    //Variables globales y locales


    static void hello_java(){
        FuncionesAlcance myGlobalvar2 = new FuncionesAlcance();
        String localvar = "Hola";
        System.out.println(localvar + " " + myGlobalvar2.globalvar);
    }
}
