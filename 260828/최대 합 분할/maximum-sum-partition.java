import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = 0;
        int[] arr = new int[n+1];
        for(int i = 1; i <= n; i++){
            arr[i] = sc.nextInt();
            m += arr[i];
        }
        final int MIN = Integer.MIN_VALUE;
        final int offset = m;
        int mxDiff = 2*m+1;
        int[][] dp = new int[n+1][mxDiff];
        for(int i = 0; i <= n; i++)
            Arrays.fill(dp[i], MIN);
        dp[0][0+offset] = 0;
        for(int i = 1; i <= n; i++){
            for(int j = -m; j <= m; j++){
                int idx = j + offset;
                if(-m <= j-arr[i] && j-arr[i] <= m && dp[i-1][idx-arr[i]] != MIN){
                    dp[i][idx] = Math.max(dp[i][idx], dp[i-1][idx-arr[i]]+arr[i]);
                }
                if(-m <= j+arr[i] && j+arr[i] <= m && dp[i-1][idx+arr[i]] != MIN){
                    dp[i][idx] = Math.max(dp[i][idx], dp[i-1][idx+arr[i]]);
                }
                if(dp[i-1][idx] != MIN){
                    dp[i][idx] = Math.max(dp[i][idx], dp[i-1][idx]);
                }
            }
        }
        System.out.println(dp[n][0+offset]);
    }
}