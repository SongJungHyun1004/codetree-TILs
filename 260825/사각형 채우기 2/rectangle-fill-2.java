import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        final int MOD = 10007;
        int n = sc.nextInt();
        long[] dp = new long[n+1];
        dp[0] = 1;
        dp[1] = 1;
        for(int i = 2; i <= n; i++){
            dp[i] = (dp[i-1]+dp[i-2]*2)%MOD;
        }
        System.out.println(dp[n]);
    }
}