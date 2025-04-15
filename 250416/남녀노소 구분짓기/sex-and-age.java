import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int g = sc.nextInt();
        int age = sc.nextInt();
        String ans = "";
        if(g == 0){
            if(age >= 19)
                ans = "MAN";
            else
                ans = "BOY";
        }else{
            if(age >= 19)
                ans = "WOMAN";
            else
                ans = "GIRL";
        }
        System.out.print(ans);
    }
}
