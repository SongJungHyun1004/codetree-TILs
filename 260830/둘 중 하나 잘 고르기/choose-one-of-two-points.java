import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] red = new int[2*n+1];
        int[] blue = new int[2*n+1];
        for (int i = 1; i <= 2 * n; i++) {
            red[i] = sc.nextInt();
            blue[i] = sc.nextInt();
        }
        int[][] dp = new int[n+1][n+1];
        for(int i = 0; i <= n; i++)
            Arrays.fill(dp[i], -1);
        dp[0][0] = 0;
        for(int i = 1; i <= n; i++){
            dp[i][0] = Math.max(dp[i][0], dp[i-1][0] + red[i]);
            dp[0][i] = Math.max(dp[0][i], dp[0][i-1] + blue[i]);
        }
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= n; j++){
                if(dp[i-1][j] != -1)
                    dp[i][j] = Math.max(dp[i][j], dp[i-1][j] + red[i+j]);
                if(dp[i][j-1] != -1)
                    dp[i][j] = Math.max(dp[i][j], dp[i][j-1] + blue[i+j]);
            }
        }
        System.out.println(dp[n][n]);
    }
}