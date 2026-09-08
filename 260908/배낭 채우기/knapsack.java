import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] w = new int[n+1];
        int[] v = new int[n+1];
        for (int i = 1; i <= n; i++) {
            w[i] = sc.nextInt();
            v[i] = sc.nextInt();
        }
        int[][] dp = new int[n+1][m+1];
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= m; j++){
                dp[i][j] = dp[i-1][j];
                if(j >= w[i])
                    dp[i][j] = Math.max(dp[i][j], dp[i-1][j-w[i]]+v[i]);
            }
        }
        System.out.println(dp[n][m]);
    }
}