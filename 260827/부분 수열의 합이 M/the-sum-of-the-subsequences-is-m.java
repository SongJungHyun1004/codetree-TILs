import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr = new int[n];
        int[] dp = new int[m+1];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        final int INF = Integer.MAX_VALUE;
        Arrays.fill(dp, INF);
        dp[0] = 0;
        for(int i = 0; i < n; i++){
            for(int j = m; j >= 1; j--){
                if(j >= arr[i]){
                    if(dp[j-arr[i]] == INF) continue;
                    dp[j] = Math.min(dp[j], dp[j-arr[i]]+1);
                }
            }
        }
        System.out.println(dp[m] != INF ? dp[m] : -1);
    }
}