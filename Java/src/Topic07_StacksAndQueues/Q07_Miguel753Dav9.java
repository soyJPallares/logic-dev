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

public class Q07_Miguel753Dav9 {

    Stack<String> web = new Stack<>();
    Queue<String> documents = new ArrayDeque<>();

    public static void main(String[] args) {
        Q07_Miguel753Dav9 objWeb = new Q07_Miguel753Dav9();
        Q07_Miguel753Dav9 objDoc = new Q07_Miguel753Dav9();
        objWeb.web.push("www.google.com");
        objWeb.web.push("www.yahoo.com");
        objWeb.web.push("www.reddit.com");
        objWeb.web.push("www.steam.com");
        objWeb.web.push("www.discord.com");

        boolean flag = true;
        while (flag) {
            Scanner capOption = new Scanner(System.in);
            System.out.print("Digite la opcion: ");
            String opc = capOption.nextLine();

            switch (opc) {
                case "forward":
                    System.out.println("Proximamente");
                    break;
                case "back":
                    browser(objWeb);
                    break;
                case "salir":
                    flag = false;
                    break;
                default:
                    objWeb.web.add(opc);
                    System.out.println("URL agregada");
            }
        }
        System.out.println(objWeb.web);

        boolean flag2 = true;
        objDoc.documents.add("Los ojos de plata");
        objDoc.documents.add("The Twisted Eyes");
        objDoc.documents.add("El cuarto armario");
        while (flag2) {
            Scanner capOption = new Scanner(System.in);
            System.out.print("Digite la opcion: ");
            String opc = capOption.nextLine();

            switch (opc) {
                case "print":
                    printer(objDoc);
                    break;
                case "salir":
                    flag2 = false;
                    break;
                default:
                    objDoc.documents.add(opc);
                    System.out.println("Documento agregado");
            }
        }
    }

    static void browser (Q07_Miguel753Dav9 objWeb) {
        if (objWeb.web.size() == 1) {
            System.out.println("No hay URL anterior");
        } else if (objWeb.web.size() > 1) {
            System.out.println(objWeb.web.get(objWeb.web.size() - 2));
            objWeb.web.pop();
        } else {
            System.out.println("La lista esta vacia");
        }
    }

    static void printer (Q07_Miguel753Dav9 objDoc) {
         if (objDoc.documents.size() < 1) {
            System.out.println("No hay documentos en la lista");
        } else {
             System.out.println(objDoc.documents.peek());
             objDoc.documents.poll();
        }
    }
}
