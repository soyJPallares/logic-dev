package Topic11_FilesHandling;
import java.io.File;         // Import the File class
import java.io.FileWriter;   // Import the FileWriter class
import java.io.IOException;  // Import the IOException class
import java.io.FileNotFoundException; // Import this class to handle errors
import java.util.Scanner;             // Import the Scanner class to read text files



public class soyJPallares {

    static void createFile(){
        File myObjFile = new File("./src/Topic11_FilesHandling/soyJPallares.txt");
        try {
            if (myObjFile.createNewFile()) {
                System.out.println("\nFile Created: \"" + myObjFile.getName() + "\"") ;
            } else {
                System.out.println("\nFile \"" + myObjFile.getName() + "\" already exists.");
            }
        } catch (IOException e){
            System.out.println("\nAn error Ocurred: " + e.getMessage());
            e.printStackTrace();
        }
    }

    static void writeFile() {
        // FileWriter will be closed automatically here
        try (FileWriter myWriter = new FileWriter("./src/Topic11_FilesHandling/soyJPallares.txt", true)) {
            myWriter.write("Jonatan Pallares\n");
            myWriter.write("48\n");
            myWriter.write("Python y Java\n");
            System.out.println("Successfully wrote to the file.");
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }

    static void readFile() {
        File myObj = new File("./src/Topic11_FilesHandling/soyJPallares.txt");

        // try-with-resources: Scanner will be closed automatically
        try (Scanner myReader = new Scanner(myObj)) {
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                System.out.println(data);
            }
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }

    public static void main(String[] args){
        createFile();
        writeFile();
        readFile();
    }
}
