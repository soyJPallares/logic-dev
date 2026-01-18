package Topic07_StacksAndQueues;

import java.util.Scanner;
import java.util.Stack;
import java.util.Queue;
import java.util.ArrayDeque;

/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */

public class Q07 {

    Stack<String> web = new Stack<>();

    public static void main(String[] args){
        menuOpciones();
    }

    static void menuWeb(){

        Q07 objWeb = new Q07();

        objWeb.web.push("www.google.com");
        objWeb.web.push("www.yahoo.com");
        objWeb.web.push("www.reddit.com");
        objWeb.web.push("www.steam.com");
        objWeb.web.push("www.discord.com");

        boolean flag = true;
        while (flag) {

            if (objWeb.web.isEmpty()) { System.out.println("La lista esta vacia"); }
            else { System.out.printf("URL: https://%s\n", objWeb.web.get(objWeb.web.size() - 1)); }

            Scanner capOption = new Scanner(System.in);
            System.out.print("Opciones: Avanzar '>>' | Retornar '<<' | Salir 'x': ");
            String opc = capOption.nextLine();

            switch (opc.toLowerCase()) {
                case ">>":
                    System.out.println("Proximamente... No es posible avanzar página.");
                    break;
                case "<<":
                    browser(objWeb);
                    break;
                case "x":
                    flag = false;
                    break;
                default:
                    objWeb.web.add(opc);
                    System.out.println("URL agregada");
            }
        }
        System.out.println(objWeb.web);

    }

    static void menu(){
        System.out.printf("\nMenu\n");
        System.out.println("1. Navegador (Pilas - Stacks)"); // Se leen igual de izquierda a derecha que de derecha a izquierda.
        System.out.println("2. Impresora (Colas - Queues)"); // Palabra que contiene exactamente las mismas letras de otra.
        System.out.println("0. Salir");
    }

    static void menuOpciones() {

        boolean flag = true;
        while (flag) {
            menu();

            Scanner capOption = new Scanner(System.in);
            System.out.print("Opcion: ");
            String opc = capOption.nextLine();

            switch (opc) {
                case "1":
                    menuWeb();
                    break;
                case "2":
                    System.out.println("Proximamente...");
//                    browser(objWeb);
                    break;
                case "0":
                    flag = false;
                    break;
                default: System.out.println("Opción errada!!!");
            }
        }
    }

    static void browser(Q07 objWeb){
        if (objWeb.web.size() == 1) {
            System.out.println("No hay URL anterior");
        }
        else if (objWeb.web.size() > 1) {
            objWeb.web.pop();
        }
        else {
            System.out.println("La lista esta vacia");
        }
    }
}