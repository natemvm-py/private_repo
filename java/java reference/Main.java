public class Main { // All java projects start with a class and is the name of the file. Every line of code that runs in Java must be inside a class. A class should always start with a capital letter
    public static void main(String[] args) { // The main() method is required and you will see it in every Java program. Any code inside the main() method will be executed.

        // Remember that every Java program has a class name which must match the filename, and that every program must contain the main() method.

        // Basics
        System.out.println("Hello World!");  // Printing syntax

        int num1 = 5;                      // Integer Variable creation
        final int num2 = 24;              // 'final' means not interchangeable. This variables value cannot be changed.
        System.out.println(num1 + num2); // Basic arithmitec.

        // Data-types
        int myNum = 5;                   // Integer (whole number)
        float myFloatNum = 5.99f;       // Float (32 bit representation of a real number, Less Space but Less Precise)
        char myLetter = 'N';           // Character (Single character data type, always uses '' instead of "")
        boolean myBool = true;        // Boolean (True or False)
        String myText = "Hello";     // String (String of characters, usually words or sentences)
        double myDouble = 51.232;   // Double (64 bit representation of a real number, More Space but More Precise)

        // Casting (Widening & Narrowing)

        // Widening Casting (automatically) - converting a smaller type to a larger type size
        // byte -> short -> char -> int -> long -> float -> double
        // Widening casting is done automatically when passing a smaller size type to a larger size type:
        System.out.println(myNum);      // Outputs: 5
        double exDouble = myNum;       // Automatic casting: int to double.
        System.out.println(exDouble); // Outputs 5.0

        // Narrowing Casting (manually) - converting a larger type to a smaller size type
        // double -> float -> long -> int -> char -> short -> byte
        // Narrowing casting must be done manually by placing the type in parentheses in front of the value:
        System.out.println(myDouble); // Outputs 51.232
        int exInt = (int) myDouble;  // Manual casting: double to int
        System.out.println(exInt);  // Outputs 51

    }
}