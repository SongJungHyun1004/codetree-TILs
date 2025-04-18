import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int num = 1;
        for(int i=0; i<N; i++){
            for(int j=0; j<i+1; j++){
                System.out.print(num+" ");
                num += 1;
            }
            System.out.println();
        }
    }
}