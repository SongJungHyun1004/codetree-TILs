import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] profit = new int[n+1];
        for (int i = 1; i <= n; i++) {
            profit[i] = sc.nextInt();
        }
        int[] dp = new int[n+1];
        Arrays.fill(dp, -1);
        dp[0] = 0;
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= n; j++){
                if(i >= j){
                    if(dp[i-j] == -1) continue;
                    dp[i] = Math.max(dp[i], dp[i-j]+profit[j]);
                }
            }
        }
        int mx = 0;
        for(int i = 1; i <= n; i++)
            mx = Math.max(mx, dp[i]);
        System.out.println(mx);
    }
}