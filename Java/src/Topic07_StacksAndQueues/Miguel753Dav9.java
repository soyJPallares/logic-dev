import java.util.Stack;
import java.util.Queue;
import java.util.ArrayDeque;

public class Miguel753Dav9 {
    public static void main(String[] args){
        Stack<Integer> pila = new Stack<>();
        pila.push(1);
        pila.push(2);
        pila.push(3);
        pila.push(4);
        pila.push(5);
        System.out.println(pila);
        System.out.println(pila.pop());
        System.out.println(pila);

        Queue<Integer> cola = new ArrayDeque<>();

        cola.add(1);
        cola.add(2);
        cola.add(3);
        cola.add(4);
        cola.add(5);
        System.out.println(cola);
        System.out.println(cola.poll());
        System.out.println(cola);
    }
}
