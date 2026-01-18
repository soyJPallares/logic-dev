package Topic02_FunctionsAndScope;

public class Q02 {
    static int numbers1to100(String text1, String text2){
         int count = 0;
         for (int i = 1; i < 101; i++ ){
             if (i % 3 == 0 && i % 5 == 0){
                 System.out.println(text1 + text2);
                 //continue;
             }
             else if (i % 3 == 0){
                 System.out.println(text1);
                 //continue;
             } else if (i % 5 == 0) {
                 System.out.println(text2);
                 //continue;
             }
             else{
                System.out.println(i);
                count += 1;
             }

         }

        return count;
    }
    public static void main(String[] args){
        System.out.println(numbers1to100("Fizz", "Buzz") );
    }
}
