package Topic03_DataStructures;

import javax.swing.*;
import java.util.Scanner;
import java.util.HashMap;

public class Q03_Miguel753Dav9 {

    HashMap<String, String> agenda = new HashMap<String, String>();

    public static void main(String[] args) {

        Q03_Miguel753Dav9 objAgenda = new Q03_Miguel753Dav9();

        generar(objAgenda);
        boolean flag = true;
        while (flag) {

            Menu();
            Scanner capOption = new Scanner(System.in);
            System.out.print("Escoga la opcion: ");
            int opc = capOption.nextInt();

            switch (opc) {
                case 1 -> Nuevo(objAgenda);
                case 2 -> Buscar(objAgenda);
                case 3 -> Editar(objAgenda);
                case 4 -> Eliminar(objAgenda);
                case 5 -> System.out.println(objAgenda.agenda);
                case 6 -> flag = false;
                default -> System.out.println("Opcion no valida");
            }
        }
    }

    static void generar(Q03_Miguel753Dav9 objAgenda) {

        objAgenda.agenda.put("Jonatan", "201");
        objAgenda.agenda.put("Miguel", "301");
        objAgenda.agenda.put("Amada", "401");
    }

    static void Menu() {
        System.out.println("Menu");
        System.out.println("1. Nuevo Contacto");
        System.out.println("2. Buscar Contacto");
        System.out.println("3. Editar Contacto");
        System.out.println("4. Eliminar Contacto");
        System.out.println("5. Listar Contacto");
        System.out.println("6. salir");
    }

    static void Nuevo(Q03_Miguel753Dav9 objAgenda) {

        //Q03 myAgenda = new Q03();

        Scanner capName = new Scanner(System.in);
        System.out.print("Digite el nombre: ");
        String name = capName.nextLine();

        Scanner capPhone = new Scanner(System.in);
        System.out.print("Digite el numero de telefono: ");
        String phone = capPhone.nextLine();

        if (phone.matches("\\d+") && phone.length() <= 11) {
            objAgenda.agenda.put(name, phone);
        }
    }
    static void Buscar(Q03_Miguel753Dav9 objAgenda){

        Scanner capName = new Scanner(System.in);
        System.out.println("Digite a el nombre a buscar: ");
        String name = capName.nextLine();
        if (objAgenda.agenda.containsKey(name)){
            System.out.println(String.format("El numero de %s es %s", name, objAgenda.agenda.get(name)));
        }
        else {
            System.out.println("El contacto no existe");
        }
    }
    static void Editar(Q03_Miguel753Dav9 objAgenda){

        Scanner capName = new Scanner(System.in);
        System.out.println("Digite la persona a editar: ");
        String name = capName.nextLine();
        if (objAgenda.agenda.containsKey(name)){

            Scanner capPhone = new Scanner(System.in);
            System.out.println("Digite el nuevo numero: ");
            String phone = capPhone.nextLine();

            if (phone.matches("\\d+") && phone.length() <= 11) {
                objAgenda.agenda.put(name, phone);
            }
            else {
                System.out.print("Solo puede digitar numeros en el numero de telefono");
            }
        }
        else {
            System.out.println("El contacto no existe");
        }
    }
    static void Eliminar(Q03_Miguel753Dav9 objAgenda){

        Scanner capName = new Scanner(System.in);
        System.out.println("Digite la persona a eliminar: ");
        String name = capName.nextLine();

        if (objAgenda.agenda.containsKey(name)){
            objAgenda.agenda.remove(name);
        }
        else {
            System.out.println("El contacto no existe");
        }
    }
}
