package Topic08_Classes;

import java.util.Scanner;
import java.util.Stack;
import java.util.Queue;
import java.util.ArrayDeque;

/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 */

class Pila {

    public Stack<String> stack = new Stack();

    public String Stack_Menu() {
        System.out.println("1. Add item");
        System.out.println("2. Delete item");
        System.out.println("3. List items");
        System.out.println("0. Return");
        return null;
    }

    public String push(String word) {
        stack.push(word);
        return null;
    }

    public String pop() {
        stack.pop();
        return null;
    }

    public String print() {
        System.out.println("Size: " + stack.size());
        System.out.println("Stack: ");

        for (int item = stack.size() - 1; item >= 0; item--) {
            System.out.println(stack.get(item));
        }

        return null;
    }

    public Pila() {

    }
}

class Cola {

    public Queue<String> queue = new ArrayDeque<>();

    public String Queue_Menu() {
        System.out.println("1. Añadir elemento");
        System.out.println("2. Eliminar elementos");
        System.out.println("3. Imprimir los elementos");
        System.out.println("0. Regresar");
        return null;
    }

    public String add(String word) {
        queue.add(word);
        return null;
    }

    public String poll() {
        queue.poll();
        return null;
    }

    public String print2() {
        System.out.println(queue.size());
        System.out.println(queue);
        return null;
    }

    public Cola() {

    }
}


public class Q08 {

    static void Menu() {
        System.out.println("1. Pilas");
        System.out.println("2. Colas");
        System.out.println("0. Salir");
    }

    public static void main(String[] args) {
        Q08 myObj = new Q08();
        Pila myStack = new Pila();
        Cola myQueque = new Cola();
        boolean flag = true;

        myQueque.add("Miguel");
        myQueque.add("Jonatan");
        myQueque.add("Amada");
        myQueque.add("Ainara");
        myQueque.add("Elena");
        myQueque.add("Barranquilla");
        myQueque.add("Medellín");
        myQueque.add("Cali");
        myQueque.add("Bogotá DC");

        myStack.push("Miguel");
        myStack.push("Jonatan");
        myStack.push("Amada");
        myStack.push("Ainara");
        myStack.push("Elena");
        myStack.push("Barranquilla");
        myStack.push("Medellín");
        myStack.push("Cali");
        myStack.push("Bogotá DC");

        while (flag) {
            Menu();

            Scanner capOption = new Scanner(System.in);
            System.out.println("Choice an option: ");

            int opc = capOption.nextInt();

            switch (opc) {

                case 1 -> {

                    boolean flag1 = true;
                    while (flag1) {
                        myStack.Stack_Menu();
                        Scanner capOption1 = new Scanner(System.in);
                        System.out.println("Choice an option: ");
                        int option1 = capOption1.nextInt();
                        switch (option1) {
                            case 1 -> {
                                Scanner capWord = new Scanner(System.in);
                                System.out.println("Write item: ");
                                String Word = capWord.nextLine();
                                myStack.push(Word);
                            }
                            case 2 -> myStack.pop();

                            case 3 -> myStack.print();

                            case 0 -> flag1 = false;
                        }
                    }
                }

                case 2 -> {
                    boolean flag2 = true;
                    while (flag2) {
                        myQueque.Queue_Menu();
                        Scanner capOption2 = new Scanner(System.in);
                        System.out.println("Choice an option: ");
                        int option2 = capOption2.nextInt();
                        switch (option2) {
                            case 1 -> {
                                Scanner capWord = new Scanner(System.in);
                                System.out.println("Write item: ");
                                String Word1 = capWord.nextLine();
                                myQueque.add(Word1);
                            }

                            case 2 -> myQueque.poll();

                            case 3 -> myQueque.print2();

                            case 0 -> flag2 = false;
                        }
                    }
                }

                case 0 -> flag = false;
            }
        }
    }
}