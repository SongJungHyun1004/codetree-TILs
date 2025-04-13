import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int n = sc.nextInt();
        char res;
        if(n >= 90){
            res = 'A';
        }else if(n >= 80){
            res = 'B';
        }else if(n >= 70){
            res = 'C';
        }else if(n >= 60){
            res = 'D';
        }else{
            res = 'F';
        }
        System.out.print(res);
    }
}