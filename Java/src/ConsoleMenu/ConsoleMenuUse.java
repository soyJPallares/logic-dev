package ConsoleMenu;

import java.util.List;

public class ConsoleMenuUse {

    public static void main(String[] args) {
        ConsoleMenu menu = new ConsoleMenu(
                "🛒 TIENDA VIRTUAL",
                List.of(
                        "Ver productos",
                        "Agregar al carrito",
                        "Ver carrito",
                        "Realizar pago",
                        "Salir"
                )
        );

        boolean running = true;

        while (running) {
            int opcion = menu.show();

            switch (opcion) {
                case 1 -> System.out.println("📦 Mostrando productos...");
                case 2 -> System.out.println("➕ Producto agregado al carrito.");
                case 3 -> System.out.println("🛒 Tu carrito está vacío.");
                case 4 -> System.out.println("💳 Procesando pago...");
                case 5 -> {
                    System.out.println("👋 ¡Hasta luego!");
                    running = false;
                }
            }
        }

        menu.close();
    }
}
