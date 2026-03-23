package Topic09_InheritanceAndPolymorphism;

import java.util.ArrayList;
import java.util.List;

//-------------------------------------------------------------------
class Employee{
//-------------------------------------------------------------------
    int id;
    String name;
    List<Employee> team;

    Employee(int id, String name){
        this.id = id;
        this.name = name;
        this.team = new ArrayList<>();
    }

    void add_team_member(Employee member){
        this.team.add(member);
    }

    void print_team(){
        System.out.println("Team: ");
        for (Employee member : this.team) {
            System.out.println(member.name);
        }
    }
}

//-------------------------------------------------------------------
class Manager extends Employee {
//-------------------------------------------------------------------
    public Manager(int id, String name) {
        super(id, name);
    }

    public void projects_coordinate(){
        System.out.println(this.name + "Está coordinando los proyectos de la empresa");
    }
}

//-------------------------------------------------------------------
class ProjectManager extends Employee {
//-------------------------------------------------------------------
    String project;

    public ProjectManager(int id, String name, String project) {
        super(id, name);
        this.project = project;
    }

    public void project_coordinate(){
        System.out.println(this.name + "Está coordinando su proyecto");
    }
}

//-------------------------------------------------------------------
class Programmer extends Employee {
//-------------------------------------------------------------------
    String language;

    public Programmer(int id, String name, String language) {
        super(id, name);
        this.language = language;
    }

    public void code() {
        System.out.println(this.name + " está programando en " + this.language + ".");
    }

    @Override
    public void add_team_member(Employee employee) {
        System.out.println("Un programador no tiene empleados a su cargo. " + employee.name + " no se añadirá.");
    }
}

public class devJPallares {

    public static void main(String[] args) {

        Manager myManager = new Manager(1, "MoureDev");

        ProjectManager myProjectManager = new ProjectManager(2, "Brais", "Proyecto 1");
        ProjectManager myProjectManager2 = new ProjectManager(3, "Moure", "Proyecto 2");

        Programmer myProgrammer = new Programmer(4, "Kontrol", "Swift");
        Programmer myProgrammer2 = new Programmer(5, "Ros", "Cobol");
        Programmer myProgrammer3 = new Programmer(6, "Bushi", "Dart");
        Programmer myProgrammer4 = new Programmer(7, "Nasos", "Python");

        myManager.add_team_member(myProjectManager);
        myManager.add_team_member(myProjectManager2);

        myProjectManager.add_team_member(myProgrammer);
        myProjectManager.add_team_member(myProgrammer2);
        myProjectManager2.add_team_member(myProgrammer3);
        myProjectManager2.add_team_member(myProgrammer4);

        myProgrammer.add_team_member(myProgrammer2);

        myProgrammer.code();
        myProjectManager.project_coordinate();
        myManager.projects_coordinate();
        myManager.print_team();
        myProjectManager.print_team();
        myProgrammer.print_team();
    }
}