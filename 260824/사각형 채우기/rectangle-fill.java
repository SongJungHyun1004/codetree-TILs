import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        final int MOD = 10007;
        int n = sc.nextInt();
        int[] dp = new int[n+1];
        if(n == 1){
            System.out.println(1);
            System.exit(0);
        }
        dp[1] = 1;
        dp[2] = 2;
        for(int i = 3; i <= n; i++){
            dp[i] = (dp[i-1]+dp[i-2])%MOD;
        }
        System.out.println(dp[n]);
    }
}