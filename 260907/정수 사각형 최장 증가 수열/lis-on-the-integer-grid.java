import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] grid = new int[n][n];
        List<int[]> pos = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                grid[i][j] = sc.nextInt();
                pos.add(new int[] {i, j, grid[i][j]});
            }
        }
        Collections.sort(pos, (o1, o2) -> o1[2]-o2[2]);
        int[][] dp = new int[n][n];
        int[] dx = {0,1,0,-1};
        int[] dy = {1,0,-1,0};
        for(int[] info: pos){
            int x = info[0], y = info[1], val = info[2];
            dp[x][y] = Math.max(dp[x][y], 1);
            for(int i = 0; i < 4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                if((0<=nx&&nx<n && 0<=ny&&ny<n) && grid[nx][ny] > grid[x][y]){
                    dp[nx][ny] = Math.max(dp[nx][ny], dp[x][y]+1);
                }
            }
        }
        int ans = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++)
                ans = Math.max(ans, dp[i][j]);
        }
        System.out.println(ans);
    }
}