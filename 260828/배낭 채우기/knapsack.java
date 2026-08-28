import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] w = new int[n];
        int[] v = new int[n];
        int[] dp = new int[m+1];
        for (int i = 0; i < n; i++) {
            w[i] = sc.nextInt();
            v[i] = sc.nextInt();
        }
        dp[0] = 0;
        for(int i = 0; i < n; i++){
            for(int j = m; j >= 1; j--){
                if(j >= w[i])
                    dp[j] = Math.max(dp[j], dp[j-w[i]]+v[i]);
            }
        }
        int mx = 0;
        for(int i = 0; i <= m; i++)
            mx = Math.max(mx, dp[i]);
        System.out.println(mx);
    }
}