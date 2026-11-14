import java.util.*;

public class Main {
    static int N, mn;
    static int[][] cost;
    static int[] select;
    static boolean[] visited;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        cost = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                cost[i][j] = sc.nextInt();
            }
        }
        visited = new boolean[N+1];
        visited[1] = true;
        select = new int[N-1];
        mn = Integer.MAX_VALUE;
        choose(0);
        System.out.println(mn);
    }

    static void choose(int depth){
        if(depth == N-1){
            int c = 0;
            int pre = 1;
            for(int i = 0; i < N-1; i++){
                int val = cost[pre-1][select[i]-1];
                if(val == 0) return;
                c += cost[pre-1][select[i]-1];
                pre = select[i];
            }
            int val = cost[pre-1][0];
            if(val == 0) return;
            c += val;
            mn = Math.min(mn, c);
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