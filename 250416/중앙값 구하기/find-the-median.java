import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int ans = 0;
        if((a < b && b < c) || (a > b && b > c))
            ans = b;
        else if((b < a && a < c) || (b > a && a > c))
            ans = a;
        else if((a < c && c < b) || (a > c && c > b))
            ans = c;
        System.out.print(ans);
    }
}
