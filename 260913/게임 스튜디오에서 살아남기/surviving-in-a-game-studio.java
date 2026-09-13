import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        final long MOD = 1_000_000_007;
        long[][][] dp = new long[n+1][4][4]; // n, 총 t, 연속 b
        dp[1][0][0] = 1;
        dp[1][1][0] = 1;
        dp[1][0][1] = 1;
        for(int i = 1; i < n; i++){
            for(int j = 0; j < 3; j++){
                for(int k = 0; k < 3; k++){
                    dp[i+1][j][0] = (dp[i+1][j][0]+dp[i][j][k])%MOD;
                    dp[i+1][j+1][0] = (dp[i+1][j+1][0]+dp[i][j][k])%MOD;
                    dp[i+1][j][k+1] = (dp[i+1][j][k+1]+dp[i][j][k])%MOD;
                }
            }
        }
        long ans = 0;
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++)
                ans = (ans + dp[n][i][j])%MOD;
        }
        System.out.println(ans);
    }
}