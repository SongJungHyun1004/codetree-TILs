import java.util.*;
public class Main {
    static int K, N;
    static int[] select;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        K = sc.nextInt();
        N = sc.nextInt();
        select = new int[N];
        choose(0, 0);
        System.out.print(sb);
    }

    static void choose(int depth, int cnt){
        if(depth == N){
            for(int i = 0; i < N; i++)
                sb.append(select[i]).append(" ");
            sb.append("\n");
            return;
        }
        for(int i = 1; i <= K; i++){
            if(depth > 0 && select[depth-1] == i){
                if(cnt + 1 < 3){
                    select[depth] = i;
                    choose(depth+1, cnt+1);
                }
            }else{
                select[depth] = i;
                choose(depth+1, 1);
            }
        }
    }
}