import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] grid = new int[n][n];
        int[][] dp = new int[n][n];
        int[] dx = {0,1,0,-1};
        int[] dy = {1,0,-1,0};
        List<int[]> cells = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            Arrays.fill(dp[i], 1);
            for (int j = 0; j < n; j++) {
                grid[i][j] = sc.nextInt();
                cells.add(new int[] {grid[i][j], i, j});
            }
        }
        Collections.sort(cells, (o1, o2) -> (o1[0] - o2[0]));
        for(int[] val: cells){
            int x = val[1], y = val[2];
            int v = val[0];
            for(int i = 0; i < 4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                if((0<=nx&&nx<n && 0<=ny&&ny<n) && v < grid[nx][ny])
                    dp[nx][ny] = Math.max(dp[nx][ny], dp[x][y]+1);
            }
        }
        int mx = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                mx = Math.max(mx, dp[i][j]);
            }
        }
        System.out.println(mx);
    }
}