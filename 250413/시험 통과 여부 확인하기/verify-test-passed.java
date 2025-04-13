import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int N = sc.nextInt();
        
        System.out.printf(N >= 80 ? "pass": "%d more score", 80-N);
    }
}