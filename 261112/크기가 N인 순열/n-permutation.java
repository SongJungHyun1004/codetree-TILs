import java.util.*;
public class Main {
    static int N;
    static int[] select;
    static boolean[] visited;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        select = new int[N];
        visited = new boolean[N+1];
        choose(0);
        System.out.print(sb);
    }

    static void choose(int depth){
        if(depth == N){
            for(int i = 0; i < N; i++)
                sb.append(select[i]).append(" ");
            sb.append("\n");
            return;
        }
        for(int i = 1; i <= N; i++){
            if(visited[i]) continue;
            visited[i] = true;
            select[depth] = i;
            choose(depth+1);
            visited[i] = false;
        }
    }
}