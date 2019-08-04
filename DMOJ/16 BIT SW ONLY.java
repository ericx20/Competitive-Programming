import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int numCases = s.nextInt();

        for (int i=0;i<numCases;i++) {
            long a=s.nextLong();
            long b=s.nextLong();
            long p=s.nextLong();

            if (a*b!=p) {
                System.out.println("16 BIT S/W ONLY");
            }
            else {
                System.out.println("POSSIBLE DOUBLE SIGMA");
            }
        }
    }
}