import java.util.ArrayList;

public class Clases {
    String name;
    String surname;
    int age;
    ArrayList<String> Lenguajes = new ArrayList<>();

    public Clases(String name, String surname, int age, ArrayList Lenguajes) {
        this.name = name;
        this.surname = surname;
        this.age = age;
        this.Lenguajes = Lenguajes;


    }
    public String printInfo() {
        return name + " " + surname + ", Edad: " + age + ",  Lenguajes de programacion: " + Lenguajes;
    }
    public static void main(String[] args){
        ArrayList<String> temp = new ArrayList<>();
        temp.add("Python");
        temp.add("Java");
        Clases objProgrammer = new Clases("Miguel", "Pallares", 12, temp);
        System.out.println(objProgrammer.printInfo());
    }
}

