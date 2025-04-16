import java.util.*;
public class Main {
    public static void main(String[] args) {
        String[] arr = new String[10];
        Scanner sc = new Scanner(System.in);
        for(int i=0; i<10; i++){
            arr[i] = sc.next();
        }
        for(int i = 9; i >= 0; i--){
            System.out.print(arr[i]);
        }
    }
}