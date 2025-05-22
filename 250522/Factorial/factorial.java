import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // Please write your code here.
        System.out.print(fact(n));
    }
    static int fact(int x){
        if(x == 1) return 1;
        return x*fact(x-1);
    }
}