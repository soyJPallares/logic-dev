package Topic08_Classes;

import java.util.ArrayList;

public class Miguel753Dav9 {
    String name;
    String surname;
    int age;
    ArrayList<String> Lenguajes = new ArrayList<>();

    public Miguel753Dav9(String name, String surname, int age, ArrayList Lenguajes) {
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
        Miguel753Dav9 objProgrammer = new Miguel753Dav9("Miguel", "Pallares", 12, temp);
        System.out.println(objProgrammer.printInfo());
    }
}

