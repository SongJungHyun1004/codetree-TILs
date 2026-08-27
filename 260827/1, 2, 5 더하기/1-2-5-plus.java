import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        final int MOD = 10007;
        int n = sc.nextInt();
        int[] num = new int[] {1, 2, 5};
        int[] dp = new int[n+1];
        dp[0] = 1;
        for(int i = 1; i <= n; i++){
            for(int j = 0; j < num.length; j++){
                if(i >= num[j]){
                    dp[i] = (dp[i] + dp[i-num[j]])%MOD;
                }
            }
        }
        System.out.println(dp[n]);
    }
}