import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int am = sc.nextInt();
        int ae = sc.nextInt();
        int bm = sc.nextInt();
        int be = sc.nextInt();
        
        System.out.print(am > bm && ae > be ? 1 : 0);
        
    }
}
