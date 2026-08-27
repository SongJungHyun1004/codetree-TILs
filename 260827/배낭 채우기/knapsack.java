import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] w = new int[n+1];
        int[] v = new int[n+1];
        int[][] dp = new int[n+1][m+1];
        for (int i = 1; i <= n; i++) {
            w[i] = sc.nextInt();
            v[i] = sc.nextInt();
        }
        for(int i = 0; i <= n; i++)
            Arrays.fill(dp[i], -1);
        dp[0][0] = 0;
        for(int i = 1; i <= n; i++){
            for(int j = 0; j <= m; j++){
                if(j >= w[i])
                    dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-w[i]]+v[i]);
                else
                    dp[i][j] = dp[i-1][j];
            }
        }
        int mx = 0;
        for(int i = 0; i <= m; i++)
            mx = Math.max(mx, dp[n][i]);
        System.out.println(mx);
    }
}