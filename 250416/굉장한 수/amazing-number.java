import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        System.out.print((N%2==1 && N%3==0) || (N%2==0 && N%5==0));
        
    }
}
