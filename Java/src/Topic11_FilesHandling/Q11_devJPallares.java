package Topic11_FilesHandling;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;


public class Q11_devJPallares {


    //  --------------------------------------------------
    //                  Add products
    //  --------------------------------------------------
    static void addProduct() {
        System.out.print("""
                --------------------------------------------------
                          Add product         \s
                --------------------------------------------------
                """
        );

        Scanner objData = new Scanner(System.in);

        System.out.print("Product name: ");
        String name = objData.nextLine();
        System.out.print("Quantity sold: ");
        String quantity = objData.nextLine();
        System.out.print("Unit price: ");
        String price = objData.nextLine();

        // FileWriter will be closed automatically here
        try (FileWriter myWriter = new FileWriter("./src/Topic11_FilesHandling/sales_devJPallares.txt", true)) {
            myWriter.write(name + ", " + quantity + ", " + price + ".0\n");
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

    }


    //  --------------------------------------------------
    //                  Find products
    //  --------------------------------------------------
    static void findProduct() {
        System.out.println("""
                --------------------------------------------------
                          Find product         \s
                --------------------------------------------------
                """
        );

        File myObjFile = new File("./src/Topic11_FilesHandling/sales_devJPallares.txt");
        List<String> lines = new ArrayList<>(); // Creamos una lista en blanco

        // try-with-resources: Scanner will be closed automatically
        try (Scanner myReader = new Scanner(myObjFile)) {
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine(); // Leemos el archivo linea por linea
                lines.add(data); // Llenamos la lista con un elemento por cada linea del archivo
            }
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

        Scanner objFind = new Scanner(System.in);
        System.out.print("Product name: ");
        String product = objFind.nextLine();
        System.out.println("Find products: ");
        // Le damos formato a la barra de titulos de la lista de productos
        System.out.printf("""
                ---------------------------------------------------------------------
                %-40s     %4s %15s%n
                ---------------------------------------------------------------------
                ""","Product","Quantity","Value"
        );

    // Recorremos la lista para imprimirla
        for (String line : lines) {
            if (line.contains(product)) {
//                System.out.println(line);
                String strips = line.strip();

                String[] products = strips.split(",");
                String name = products[0];
                int quantity = Integer.parseInt(products[1].strip());
                float price = Float.parseFloat(products[2].strip());

                System.out.printf("%-40s      %4d    $%,14.1f%n",name,quantity,price);
            }
        }
    }


    //  --------------------------------------------------
    //                  Update products
    //  --------------------------------------------------
    static void updateProduct() {
        System.out.print("""
                --------------------------------------------------
                          Update product         \s
                --------------------------------------------------
                """
        );
    }


    //  --------------------------------------------------
    //                  Delete products
    //  --------------------------------------------------
    static void deleteProduct() {
        System.out.print("""
                --------------------------------------------------
                          Delete product         \s
                --------------------------------------------------
                """
        );
    }


    //  --------------------------------------------------
    //                  Products list
    //  --------------------------------------------------
    static void productList() {
        System.out.print("""
                --------------------------------------------------
                          Products list         \s
                """
        );

        File myObjFile = new File("./src/Topic11_FilesHandling/sales_devJPallares.txt");
        List<String> lines = new ArrayList<>(); // Creamos una lista en blanco

        // try-with-resources: Scanner will be closed automatically
        try (Scanner myReader = new Scanner(myObjFile)) {
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine(); // Leemos el archivo linea por linea
                lines.add(data); // Llenamos la lista con un elemento por cada linea del archivo
            }
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

        // Le damos formato a la barra de titulos de la lista de productos
        System.out.printf("""
                ---------------------------------------------------------------------
                %-40s     %4s %15s
                ---------------------------------------------------------------------
                ""","Product","Quantity","Value"
        );

        // Recorremos la lista para imprimirla
        for (String line : lines) {
            String strips = line.strip();

            String[] products = strips.split(",");
            String name = products[0];
            int quantity = Integer.parseInt(products[1].strip());
            float price = Float.parseFloat(products[2].strip());
            // Le damos formato a la salida de la lista de productos
            System.out.printf("%-40s      %4d    $%,14.1f%n",name,quantity,price);
        }
    }


    //  --------------------------------------------------
    //                  Sales by product
    //  --------------------------------------------------
    static void salesByProduct() {
        System.out.print("""
                --------------------------------------------------
                          Sales by product         \s
                --------------------------------------------------
                """
        );
    }


    //  --------------------------------------------------
    //                  Total sales
    //  --------------------------------------------------
    static void totalSales() {
        System.out.print("""
                --------------------------------------------------
                          Total sales         \s
                --------------------------------------------------
                """
        );
    }



    //---------------------------------------------------
    // Create File Method
    //---------------------------------------------------

    static void createFile() {

        //---------------------------------------------------
        // Create File "Object"
        // [Specify path,
        // if no-path at create file,
        // File creates it in java project root Path]
        //---------------------------------------------------
        File myObjFile = new File("./src/Topic11_FilesHandling/sales_devJPallares.txt");

        try {
            if (myObjFile.createNewFile()) {
                System.out.println("\nFile Created: \"" + myObjFile.getName() + "\"");
                initFileUpdate();
            } else {
                System.out.println("\nFile \"" + myObjFile.getName() + "\" already exists.");
            }
        } catch (IOException e) {
            System.out.println("\nAn error Ocurred: " + e.getMessage());
            e.printStackTrace();
        }
    }

    static void initFileUpdate(){
        // FileWriter will be closed automatically here
        try (FileWriter myWriter = new FileWriter("./src/Topic11_FilesHandling/sales_devJPallares.txt")) {
            myWriter.write("Procesador AMD Ryzen 9, 15, 2450000.0\n");
            myWriter.write("Procesador Intel Core i9, 12, 2410000.0\n");
            myWriter.write("Tarjeta de Video NVIDIA RTX, 8, 6550000.0\n");
            myWriter.write("Tarjeta de Video AMD Radeon, 10, 3890000.0\n");
            myWriter.write("Memoria RAM Corsair DDR5, 45, 515000.0\n");
            myWriter.write("Disco SSD Samsung NVMe, 30, 720000.0\n");
            myWriter.write("Placa Base ASUS ROG, 7, 2050000.0\n");
            myWriter.write("Fuente de Poder EVGA, 22, 550000.0\n");
            myWriter.write("Gabinete NZXT, 14, 740000.0\n");
            myWriter.write("Refrigeración Líquida Corsair, 18, 775000.0\n");
            myWriter.write("Monitor LG UltraGear, 25, 1230000.0\n");
            myWriter.write("Teclado Mecánico Logitech, 20, 940000.0\n");
            myWriter.write("Mouse Razer DeathAdder, 35, 610000.0\n");
            myWriter.write("Disco Duro Seagate, 12, 820000.0\n");
            myWriter.write("Tarjeta de Sonido Creative, 5, 1430000.0\n");
            myWriter.write("Mando Xbox Wireless, 50, 245000.0\n");
            myWriter.write("Cámara Web Logitech, 40, 285000.0\n");
            myWriter.write("Auriculares HyperX Cloud, 28, 405000.0\n");
            myWriter.write("Pasta Térmica Thermal Grizzly, 100, 51000.0\n");
            myWriter.write("Adaptador Wi-Fi TP-Link, 15, 185000.0\n");
            System.out.println("Successfully wrote to the file.");
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }


    //---------------------------------------------------
    // Menu Method
    //---------------------------------------------------

    static void menu() {
        System.out.println("1. Add product");
        System.out.println("2. View product");
        System.out.println("3. Update product");
        System.out.println("4. Delete product");
        System.out.println("5. Product list");
        System.out.println("6. Sales by product");
        System.out.println("7. Total sales");
        System.out.println("0. Quit");
    }

    public static void main(String[] args){
        createFile();


        //----------------------------------------------------------------------
        // Options Menu:
        //----------------------------------------------------------------------
        boolean flag = true;

        while (flag) {
            menu();
            Scanner capOption = new Scanner(System.in);
            System.out.print("Choose an option: ");
            String opc = capOption.nextLine();
            String x;

            switch (opc) {
                case "1":
                    addProduct();
                    System.out.print("Press [Enter] key to continue... ");
                    x = capOption.nextLine();
                    break;
                case "2":
                    findProduct();
                    System.out.print("\nPress [Enter] key to continue... ");
                    x = capOption.nextLine();
                    break;
                case "3":
                    updateProduct();
                    System.out.print("Press [Enter] key to continue... ");
                    x = capOption.nextLine();
                    break;
                case "4":
                    deleteProduct();
                    System.out.print("Press [Enter] key to continue... ");
                    x = capOption.nextLine();
                    break;
                case "5":
                    productList();
                    System.out.print("\nPress [Enter] key to continue... ");
                    x = capOption.nextLine();
                    break;
                case "6":
                    salesByProduct();
                    System.out.print("Press [Enter] key to continue... ");
                    x = capOption.nextLine();
                    break;
                case "7":
                    totalSales();
                    System.out.print("Press [Enter] key to continue... ");
                    x = capOption.nextLine();
                    break;
                case "0":
                    flag = false;
                    break;
                default:
                    System.out.print("Not Support Option...\nPress [Enter] key to continue... ");
                    x = capOption.nextLine();
                    break;
            }
        }
    }
}