import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        final int MOD = 1_000_000_007;
        int[][] dp = new int[n+1][10];
        for(int i = 1; i <= 9; i++)
            dp[1][i] = 1;
        for(int i = 2; i <= n; i++){
            for(int j = 0; j <= 9; j++){
                for(int k = 0; k <= 9; k++){
                    if(Math.abs(j-k) != 1) continue;
                    dp[i][k] = (dp[i][k] + dp[i-1][j]) % MOD;
                }
            }
        }
        int ans = 0;
        for(int i = 0; i <= 9; i++)
            ans = (ans + dp[n][i]) % MOD;
        System.out.println(ans);
    }
}