import java.util.*;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        System.out.print(a+" ");
        while(a <= b){
            if(a % 2 == 1)
                a *= 2;
            else
                a += 3;
            if(a > b)
                break;
            System.out.print(a+" ");
        }
    }
}