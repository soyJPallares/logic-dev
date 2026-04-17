package Topic11_FilesHandling;
import java.io.File;
import java.io.IOException;



public class soyJPallares {


    static File myObjFile = new File("./src/Topic11_FilesHandling/soyJPallares.txt");

    static void createFile(){
        try {
            if (myObjFile.createNewFile()) {
                System.out.println("\nFile Created: " + myObjFile.getName());
            } else {
                System.out.println("\nFile " + myObjFile.getName() + " already exists.");
            }
        } catch (IOException e){
            System.out.println("\nAn error Ocurred: " + e.getMessage());
            e.printStackTrace();
        }
    }

    public static void main(String[] args){
        createFile();
    }

}
