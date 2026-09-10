import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int offset = 0;
        int[] arr = new int[n+1];
        for(int i = 1; i <= n; i++){
            arr[i] = sc.nextInt();
            offset += arr[i];
        }
        int m = offset*2;
        int[][] dp = new int[n+1][m+1];
        int MIN = Integer.MIN_VALUE;
        for(int i = 0; i <= n; i++)
            Arrays.fill(dp[i], MIN);
        dp[0][0+offset] = 0;
        for(int i = 1; i <= n; i++){
            for(int j = -offset; j <= offset; j++){
                int idx = j+offset;
                if(0 <= idx-arr[i] && idx-arr[i] <= m && dp[i-1][idx-arr[i]] != MIN)
                    dp[i][idx] = Math.max(dp[i][idx], dp[i-1][idx-arr[i]]+arr[i]);
                if(0 <= idx+arr[i] && idx+arr[i] <= m && dp[i-1][idx+arr[i]] != MIN)
                    dp[i][idx] = Math.max(dp[i][idx], dp[i-1][idx+arr[i]]);
                if(dp[i-1][idx] != MIN)
                    dp[i][idx] = Math.max(dp[i][idx], dp[i-1][idx]);
            }
        }
        System.out.println(dp[n][0+offset]);
    }
}