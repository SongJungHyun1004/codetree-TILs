import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        final int MOD = 10007;
        int n = sc.nextInt();
        int[] dp = new int[n+1];
        dp[0] = 1;
        dp[2] = 1;
        if(n == 2){
            System.out.println(1);
            System.exit(0);
        }
        for(int i = 3; i <= n; i++){
            dp[i] = (dp[i-2]+dp[i-3])%MOD;
        }
        System.out.println(dp[n]);
    }
}