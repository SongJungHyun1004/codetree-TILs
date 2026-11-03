import java.util.Scanner;

public class Main {
    static int K, N;
    static int[] select;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        K = sc.nextInt();
        N = sc.nextInt();
        select = new int[N];
        choose(0);
        System.out.println(sb);
    }

    static void choose(int depth){
        if(depth == N){
            for(int i = 0; i < N; i++)
                sb.append(select[i]).append(" ");
            sb.append("\n");
            return;
        }
        for(int i = 1; i <= K; i++){
            select[depth] = i;
            choose(depth+1);
        }
    }
}