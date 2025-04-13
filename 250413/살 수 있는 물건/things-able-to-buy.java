import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int n = sc.nextInt();
        String res = "no";
        if(n >= 3000){
            res = "book";
        }else if(n >= 1000){
            res = "mask";
        }
        System.out.print(res);
    }
}