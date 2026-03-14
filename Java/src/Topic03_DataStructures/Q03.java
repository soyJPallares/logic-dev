package Topic03_DataStructures;

import javax.swing.*;
import java.util.Scanner;
import java.util.HashMap;

public class Q03 {

    HashMap<String, String> agenda = new HashMap<>();

    public static void main(String[] args) {

        Q03 objAgenda = new Q03();

        Generar(objAgenda);
        boolean flag = true;
        while (flag) {

            Menu();
            Scanner capOption = new Scanner(System.in);
            System.out.print("Escoja la opción: ");
            int opc = capOption.nextInt();

            switch (opc) {
                case 1 -> Nuevo(objAgenda);
                case 2 -> Buscar(objAgenda);
                case 3 -> Editar(objAgenda);
                case 4 -> Eliminar(objAgenda);
                case 5 -> Listar(objAgenda);
                case 6 -> flag = false;
                default -> System.out.println("Opción no válida");
            }
        }
    }


    static void Generar(Q03 objAgenda) {
        objAgenda.agenda.put("Jonatan", "300 598 1009");
        objAgenda.agenda.put("Miguel", "300 445 1231");
        objAgenda.agenda.put("Amada", "301 445 4562");
        objAgenda.agenda.put("Elena", "302 445 1203");
        objAgenda.agenda.put("Ainara", "311 445 5694");
        objAgenda.agenda.put("Alanna", "312 445 8795");
        objAgenda.agenda.put("Cris", "313 445 9578");
        objAgenda.agenda.put("Yaireth", "320 454 7895");
        objAgenda.agenda.put("Poncho", "321 457 8495");
        objAgenda.agenda.put("Hilda", "317 223 7548");
    }


    static void Listar(Q03 objAgenda) {

        System.out.println("\nContactos\n");
        objAgenda.agenda.forEach((name, phone) -> System.out.printf("%s : %s\n", name, phone));

    }


    static void Menu() {
        System.out.println("\nContactos\n");
        System.out.println("1. Nuevo");
        System.out.println("2. Buscar");
        System.out.println("3. Editar");
        System.out.println("4. Eliminar");
        System.out.println("5. Listar");
        System.out.println("6. salir");
    }


    static void Nuevo(Q03 objAgenda) {
        Scanner capData = new Scanner(System.in);

        System.out.print("Nombre: ");
        String name = capData.nextLine();

        System.out.print("Teléfono: ");
        String phone = capData.nextLine();

        if (phone.matches("\\d+") && (phone.length() > 0 && phone.length() <= 11)) {
            objAgenda.agenda.put(name, phone);
        }
    }


    static void Buscar(Q03 objAgenda){
        Scanner capData = new Scanner(System.in);

        System.out.print("Nombre: ");
        String name = capData.nextLine();

        if (objAgenda.agenda.containsKey(name)){
            System.out.printf("%s : %s\n", name, objAgenda.agenda.get(name));
        }
        else {
            System.out.println("\nEl contacto no existe");
        }
    }


    static void Editar(Q03 objAgenda){

        Scanner capData = new Scanner(System.in);
        System.out.print("Nombre: ");
        String name = capData.nextLine();

        if (objAgenda.agenda.containsKey(name)){

            //Scanner capPhone = new Scanner(System.in);
            System.out.print("Nuevo número: ");
            String phone = capData.nextLine();

            if (phone.matches("\\d+") && (phone.length() > 0 && phone.length() <= 11)) {
                objAgenda.agenda.put(name, phone);
                System.out.println("\n¡Contacto actualizado!\n");
            }
            else {
                System.out.println("\nDigita sólo números\n");
            }
        }
        else {
            System.out.println("\nEl contacto no existe\n");
        }
    }


    static void Eliminar(Q03 objAgenda) {

        Scanner capName = new Scanner(System.in);
        System.out.print("Nombre: ");
        String name = capName.nextLine();

        if (objAgenda.agenda.containsKey(name)){
            objAgenda.agenda.remove(name);
            System.out.println("\nContacto eliminado\n");
        }
        else {
            System.out.println("\nEl contacto no existe\n");
        }
    }
}