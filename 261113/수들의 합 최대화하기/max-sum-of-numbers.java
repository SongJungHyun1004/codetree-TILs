import java.util.*;
public class Main {
    static int N, mx;
    static int[][] grid;
    static int[] col;
    static boolean[] visited;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        grid = new int[N][N];
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                grid[i][j] = sc.nextInt();
        col = new int[N];
        visited = new boolean[N];
        choose(0);
        System.out.println(mx);
    }

    static void choose(int row){
        if(row == N){
            int sum = 0;
            for(int i = 0; i < N; i++){
                int j = col[i];
                sum += grid[i][j];
            }
            mx = Math.max(mx, sum);
            return;
        }
        for(int i = 0; i < N; i++){
            if(visited[i]) continue;
            visited[i] = true;
            col[row] = i;
            choose(row+1);
            visited[i] = false;
        }
    }
}