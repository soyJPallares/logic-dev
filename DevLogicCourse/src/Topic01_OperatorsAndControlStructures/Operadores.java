package Topic01_OperatorsAndControlStructures;

public class Operadores {

    public static void main(String[] args) {
        //Operadores Aritmeticos

        int a = 10;
        int b = 3;

        System.out.println("a + b : " + (a + b));
        System.out.println("a - b : " + (a - b));
        System.out.println("a * b : " + (a * b));
        System.out.println("a / b : " + (a / b));
        System.out.println("a % b : " + (a % b));

        float d = 10.0f;
        float e = 3.0f;

        System.out.println("d / e : " + (d / e));

        //Operadores de comparacion

        System.out.println("Igualdad: a == b: " + (a == b));
        System.out.println("Desigualdad: a != b: " + (a != b));
        System.out.println("Mayor que: a > b: " + (a > b));
        System.out.println("Menor que: a < b: " + (a < b));
        System.out.println("Mayor igual que: a >= b: " + (a >= b));
        System.out.println("Menor igual que: a <= b: " + (a <= b));

        //Operadores lógicos
        System.out.println("AND &&: 10 + 3 == 13 && 5 - 1 == 4 es " + (10 + 3 == 13 && 5 - 1 == 4));
        System.out.println("OR ||: 10 + 3 == 14 || 5 - 1 == 4 es " + (10 + 3 == 14 || 5 - 1 == 4));
        System.out.println("NOT !: ! 10 + 3 == 14 es " + !(10 + 3 == 14));

        //Operadores de asignacion
        int c = 5;
        ++c;
        System.out.println("c + 1 : " + c);
        --c;
        System.out.println("c - 1 : " + c);

        c += 1;
        System.out.println(c);
        c -= 1;
        System.out.println(c);
        c *= 1;
        System.out.println(c);
        c /= 1;
        System.out.println(c);
        c %= 1;
        System.out.println(c);
        double ex = Math.pow(c, 2);
        System.out.println(ex);
        float f = 5.0f;
        float g = 2.0f;
        System.out.println(f / g);

        //Operadores de identidad no existe pero este es el equivalente:
        /*En Java, cuando usas == con objetos, lo que estás comparando es su identidad.
        Es decir, si ambos apuntan a la misma dirección física en la memoria RAM.
        */
        String s1 = new String("Hola");
        String s2 = new String("Hola");
        String s3 = s1;

        System.out.println(s1 == s2); // false (Contenido igual, pero objetos diferentes)
        System.out.println(s1 == s3); // true  (Son exactamente el mismo objeto)

        //Operadores de pertenencia
        String frase = "Java es genial";
        System.out.println(frase.contains("genial")); // true

        //Operadores de bits

        int n = 10;
        int m = 3;
        int resultAND = 10 & 3;
        System.out.println("AND: 10 & 3 = " + resultAND);
        int resultOR = 10 | 3;
        System.out.println("OR: 10 | 3 = " + resultOR);
        int resultXOR = 10 ^ 3;
        System.out.println("XOR: 10 ^ 3 = " + resultXOR);
        int resultNOT = ~10;
        System.out.println("NOT: ~10 = " + resultNOT);
        int resultDesDerecha = 10 >> 3;
        System.out.println("Desplazamiento a la derecha: 10 >> 3 = " + resultDesDerecha);
        int resultDesIzquierda = 10 << 3;
        System.out.println("Desplazamiento a la izquierda: 10 << 3 = " + resultDesIzquierda);

        //Estructura de datos

        //Condicionales

        String my_string = "Miguel";

        if (my_string == "Miguel"){
            System.out.println("my_string es 'Miguel'");
        }
        else if (my_string == "Pallares"){
            System.out.println("my_string es Pallares");
        }
        else {
            System.out.println("my_string no es ni 'Miguel' ni 'Pallares'");
        }

        //Iterativas
        for (int i =  0; i < 11; i++) {
            System.out.println(i);
        }

        int i2 = 0;
        while (i2 < 11){
            System.out.println(i2);
            i2++;
        }

        //Manejo de excepciones
        try {
            System.out.println(10 / 0);
        } catch (Exception e1) {
            System.out.println("Se ha generado un error");
        }
        finally {
            System.out.println("Ha finalizado el manejo de excepciones");
        }

    }
}