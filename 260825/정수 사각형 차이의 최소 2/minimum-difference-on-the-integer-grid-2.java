import java.util.*;

public class Main {
    static int n;
    static int[][] grid, dp;
    static int low = 101;
    static int high = 0;
    static int mn = Integer.MAX_VALUE;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        grid = new int[n][n];
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                grid[i][j] = sc.nextInt();
                low = Math.min(low, grid[i][j]);
                high = Math.max(high, grid[i][j]);
            }
        }
        for(int lower = low; lower <= high; lower++){
            int upper = solve(lower);
            mn = Math.min(mn, upper-lower);
        }
        System.out.println(mn);
    }

    static int solve(int lower){
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] < lower)
                    grid[i][j] = Integer.MAX_VALUE;
            }
        }
        dp = new int[n][n];
        for(int i = 0; i < n; i++){
            Arrays.fill(dp[i], Integer.MAX_VALUE);
        }
        dp[0][0] = grid[0][0];
        for(int i = 1; i < n; i++)
            dp[i][0] = Math.max(dp[i-1][0], grid[i][0]);
        for(int j = 1; j < n; j++)
            dp[0][j] = Math.max(dp[0][j-1], grid[0][j]);
        for(int i = 1; i < n; i++){
            for(int j = 1; j < n; j++){
                dp[i][j] = Math.max(Math.min(dp[i-1][j], dp[i][j-1]), grid[i][j]);
            }
        }
        return dp[n-1][n-1];
    }
}