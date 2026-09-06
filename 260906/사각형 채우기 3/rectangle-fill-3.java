import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        final long MOD = 1_000_000_007;
        long[] dp = new long[n+1];
        Arrays.fill(dp, -1);
        dp[0] = 1;
        dp[1] = 2;
        for(int i = 2; i <= n; i++){
            dp[i] = (dp[i-1]*2+dp[i-2]*3)%MOD;
            for(int j = i-3; j >= 0; j--){
                dp[i] = (dp[i] + dp[j]*2)%MOD;
            }
        }
        System.out.println(dp[n]);
    }
}