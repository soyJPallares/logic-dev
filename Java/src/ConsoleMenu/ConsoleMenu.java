package ConsoleMenu;

import java.util.List;
import java.util.Scanner;

public class ConsoleMenu {

    private final String title;
    private final List<String> options;
    private final Scanner scanner;

    public ConsoleMenu(String title, List<String> options) {
        this.title = title;
        this.options = options;
        this.scanner = new Scanner(System.in);
    }

    public ConsoleMenu(List<String> options) {
        this("=== MENÚ ===", options);
    }

    public int show() {
        int choice = -1;

        while (choice < 1 || choice > options.size()) {
            printMenu();
            System.out.print("Seleccione una opción: ");

            if (scanner.hasNextInt()) {
                choice = scanner.nextInt();
                if (choice < 1 || choice > options.size()) {
                    System.out.println("❌ Opción inválida. Intente de nuevo.\n");
                }
            } else {
                System.out.println("❌ Entrada inválida. Ingrese un número.\n");
                scanner.next(); // limpiar entrada
            }
        }

        return choice;
    }

//    public void clearScreen() {
//        try {
//            String os = System.getProperty("os.name").toLowerCase();
//
//            if (os.contains("win")) {
//                new ProcessBuilder("cmd", "/c", "cls")
//                        .inheritIO()
//                        .start()
//                        .waitFor();
//            } else {
//                new ProcessBuilder("clear")
//                        .inheritIO()
//                        .start()
//                        .waitFor();
//            }
//        } catch (Exception e) {
//            // Si falla, imprime líneas en blanco como fallback
//            for (int i = 0; i < 50; i++) System.out.println();
//        }
//    }

    private void printMenu() {
//        clearScreen();
        System.out.println("\n" + "─".repeat(30));
        System.out.println("  " + title);
        System.out.println("─".repeat(30));
        for (int i = 0; i < options.size(); i++) {
            System.out.printf("  %d. %s%n", i + 1, options.get(i));
        }
        System.out.println("─".repeat(30));
    }

    public void close() {
        scanner.close();
    }
}
/*
    // ── Ejemplo de uso ──────────────────────────────────────────
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
```
*/

//---------------------------------------------------------------------------------------------
//*********************************************************************************************
//---------------------------------------------------------------------------------------------

/*
        ## Características de la clase

**Constructores disponibles:**
        - `ConsoleMenu(String title, List<String> options)` — con título personalizado
- `ConsoleMenu(List<String> options)` — usa un título por defecto

**Método principal:**
        - `show()` → muestra el menú, valida la entrada y **retorna el número de opción elegida** (1-based)

        **Validaciones incluidas:**
        - Rechaza números fuera del rango válido
- Rechaza entradas no numéricas (letras, símbolos)
- Repite el menú hasta recibir una opción válida

**Ejemplo de salida en consola:**
        ```
        ──────────────────────────────
        🛒 TIENDA VIRTUAL
──────────────────────────────
        1. Ver productos
  2. Agregar al carrito
  3. Ver carrito
  4. Realizar pago
  5. Salir
──────────────────────────────
Seleccione una opción:

 */