import java.util.*;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        while(true){
            int n = sc.nextInt();
            if(n == 25){
                System.out.println("Good");
                break;
            }
            if(n > 25)
                System.out.println("Lower");
            else
                System.out.println("Higher");
        }
    }
}