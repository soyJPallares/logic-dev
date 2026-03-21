package Topic08_Classes;

import java.util.ArrayList;
import java.util.List;

// Ejercicio

class Programmer {
    String name;
    String surname = "";
    int age;
    List<String> languages;

    public Programmer(String name, int age, List<String> languages){
        this.name = name;
        this.age = age;
        this.languages = languages;
    }

    public void printer() {
        System.out.println("Nombre: " + this.name + "| Apellidos: " + this.surname +
                "| Edad: " + this.age + " | Lenguajes: " + this.languages);
    }
}

public class devJPallares {

    public static void main(String[] args) {

        List<String> languages = new ArrayList<>(List.of("Pascal", "C", "C++", "Cobol", "Visual Basic 6.0", "Visual FoxPro 9.0", "MySQL", "Python", "Java"));

        Programmer objDev = new Programmer("Jonatan", 45, languages);
        objDev.printer();

        objDev.surname = "Pallares";
        objDev.printer();

        objDev.age = 48;
        objDev.printer();
    }
}

