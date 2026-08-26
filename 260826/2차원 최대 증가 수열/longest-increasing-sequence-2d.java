import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] grid = new int[n][m];
        int[][] dp = new int[n][m];
        for (int i = 0; i < n; i++){
            Arrays.fill(dp[i], -1);
            for (int j = 0; j < m; j++)
                grid[i][j] = sc.nextInt();
        }
        dp[0][0] = 1;
        for(int i = 1; i < n; i++){
            for(int j = 1; j < m; j++){
                for(int k = 0; k < i; k++){
                    for(int l = 0; l < j; l++){
                        if(dp[k][l] == -1) continue;
                        if(grid[k][l] < grid[i][j]){
                            dp[i][j] = Math.max(dp[i][j], dp[k][l]+1);
                        }
                    }
                }
            }
        }
        int mx = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                mx = Math.max(mx, dp[i][j]);
            }
        }
        System.out.println(mx);
    }
}