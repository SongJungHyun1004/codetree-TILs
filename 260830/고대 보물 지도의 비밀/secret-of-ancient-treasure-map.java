import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int[] arr = new int[N+1];
        for (int i = 1; i <= N; i++) {
            arr[i] = sc.nextInt();
        }
        int[][] dp = new int[N+1][K+1];
        final int MIN = Integer.MIN_VALUE;
        for(int i = 0; i <= N; i++)
            Arrays.fill(dp[i], MIN);
        for(int i = 1; i <= N; i++){
            if(arr[i] >= 0){
                dp[i][0] = arr[i];
                for(int j = 0; j <= K; j++){
                    if(dp[i-1][j] != MIN)
                        dp[i][j] = Math.max(dp[i][j], dp[i-1][j] + arr[i]);
                }
            } else {
                dp[i][1] = arr[i];
                for(int j = 1; j <= K; j++){
                    if(dp[i-1][j-1] != MIN)
                        dp[i][j] = Math.max(dp[i][j], dp[i-1][j-1] + arr[i]);
                }
            }
        }
        int mx = MIN;
        for(int i = 0; i <= N; i++){
            for(int j = 0; j <= K; j++)
                mx = Math.max(mx, dp[i][j]);
        }
        System.out.println(mx);
    }
}