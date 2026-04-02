package Topic09_InheritanceAndPolymorphism;

import java.util.ArrayList;
import java.util.List;

class Employee_M753D9 {
    int id;
    String name;
    List<Employee_M753D9> team;
    public Employee_M753D9(int id, String name){
        this.id = id;
        this.name = name;
        this.team = new ArrayList<>();
    }
    public void add_team_member(Employee_M753D9 member){
        this.team.add(member);
    }
    public void print_employees(){
        for(Employee_M753D9 member : team){
            System.out.println(member.name);
        }
    }
}
class Manager_M753D9 extends Employee_M753D9{
    public Manager_M753D9(int id, String name){super(id, name);}

    public void coordinate_projects(){
        System.out.println(this.name + "esta coordinando la empresa");
    }
}

class Project_Manager_M753D9 extends Employee_M753D9{
    String project;

    public Project_Manager_M753D9(int id, String name, String project){
        super(id, name);
        this.project = project;
    }
    public void project_coordinate(){
        System.out.println(this.name + "esta coordinando su proyecto");
    }
}

class Programmer_M753D9 extends Employee_M753D9{
    String language;

    public Programmer_M753D9(int id, String name, String language){
        super(id, name);
        this.language = language;
    }

    public void code(){System.out.println(this.name + " esta programando en " + this.language + ".");}

    @Override
    public void add_team_member(Employee_M753D9 employee){
        System.out.println("Un programador no tiene empleados a su cargo. " + employee.name + " no se añadira.");
    }
}

public class Q09_Miguel753Dav9 {
    public static void main(String[] args) {

        Manager_M753D9 myManager = new Manager_M753D9(1, "MoureDev");

        Project_Manager_M753D9 myProjectManager = new Project_Manager_M753D9(2, "Brais", "Proyecto 1");
        Project_Manager_M753D9 myProjectManager2 = new Project_Manager_M753D9(3, "Moure", "Proyecto 2");

        Programmer_M753D9 myProgrammer = new Programmer_M753D9(4, "Kontrol", "Swift");
        Programmer_M753D9 myProgrammer2 = new Programmer_M753D9(5, "Ros", "Cobol");
        Programmer_M753D9 myProgrammer3 = new Programmer_M753D9(6, "Bushi", "Dart");
        Programmer_M753D9 myProgrammer4 = new Programmer_M753D9(7, "Nasos", "Python");

        myManager.add_team_member(myProjectManager);
        myManager.add_team_member(myProjectManager2);

        myProjectManager.add_team_member(myProgrammer);
        myProjectManager.add_team_member(myProgrammer2);
        myProjectManager2.add_team_member(myProgrammer3);
        myProjectManager2.add_team_member(myProgrammer4);

        myProgrammer.add_team_member(myProgrammer2);

        myProgrammer.code();
        myProjectManager.project_coordinate();
        myManager.coordinate_projects();
        myManager.print_employees();
        myProjectManager.print_employees();
        myProgrammer.print_employees();
    }
}
