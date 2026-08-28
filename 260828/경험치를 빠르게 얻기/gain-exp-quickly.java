import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] exp = new int[n];
        int[] time = new int[n];
        int total = 0;
        for (int i = 0; i < n; i++) {
            exp[i] = sc.nextInt();
            total += exp[i];
            time[i] = sc.nextInt();
        }
        int[] dp = new int[total+1];
        final int INF = Integer.MAX_VALUE;
        Arrays.fill(dp, INF);
        dp[0] = 0;
        for(int i = 0; i < n; i++){
            for(int j = total; j >= 1; j--){
                if(j >= exp[i]){
                    if(dp[j-exp[i]] == INF) continue;
                    dp[j] = Math.min(dp[j], dp[j-exp[i]]+time[i]);
                }
            }
        }
        int mn = INF;
        for(int i = m; i <= total; i++){
            mn = Math.min(mn, dp[i]);
        }
        System.out.println(mn != INF ? mn : -1);
    }
}