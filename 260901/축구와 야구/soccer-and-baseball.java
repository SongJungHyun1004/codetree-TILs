import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] soccer = new int[N+1];
        int[] baseball = new int[N+1];
        int[][][] dp = new int[N+1][12][10];
        for (int i = 1; i <= N; i++) {
            soccer[i] = sc.nextInt();
            baseball[i] = sc.nextInt();
        }
        for(int i = 1; i <= N; i++){
            for(int j = 0; j <= 11; j++){
                for(int k = 0; k <= 9; k++){
                    dp[i][j][k] = Math.max(dp[i][j][k], dp[i-1][j][k]);
                    if(j > 0)
                        dp[i][j][k] = Math.max(dp[i][j][k], dp[i-1][j-1][k] + soccer[i]);
                    if(k > 0)
                        dp[i][j][k] = Math.max(dp[i][j][k], dp[i-1][j][k-1] + baseball[i]);
                }
            }
        }
        System.out.println(dp[N][11][9]);
    }
}