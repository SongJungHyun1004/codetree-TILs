import java.util.Scanner;

public class Main {
    static int K, N;
    static int[] select;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        K = sc.nextInt();
        N = sc.nextInt();
        select = new int[N];
        choose(0);
    }

    static void choose(int depth){
        if(depth == N){
            for(int i = 0; i < N; i++)
                System.out.print(select[i]+" ");
            System.out.println();
            return;
        }
        for(int i = 1; i <= K; i++){
            select[depth] = i;
            choose(depth+1);
        }
    }
}