import java.util.*;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int three = 0, five = 0;
        for(int i=0; i<10; i++){
            int n = sc.nextInt();
            if(n%3==0)
                three += 1;
            if(n%5==0)
                five += 1;
        }
        System.out.print(three+" "+five);
    }
}