import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int n = sc.nextInt();
        String res;
        if(n < 0){
            res = "ice";
        } else if(n >= 100){
            res = "vapor";
        }else{
            res = "water";
        }
        System.out.print(res);
    }
}