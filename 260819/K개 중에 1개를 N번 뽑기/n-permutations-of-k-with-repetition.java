import java.util.Scanner;

public class Main {
    static int[] select;
    static int k, n;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        k = sc.nextInt();
        n = sc.nextInt();
        select = new int[n];
        choose(0);
    }

    static void choose(int depth){
        if(depth == n){
            for(int i = 0; i < n; i++)
                System.out.print(select[i]+" ");
            System.out.println();
            return;
        }
        for(int i = 1; i <= k; i++){
            select[depth] = i;
            choose(depth + 1);
        }
    }
}