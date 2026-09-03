import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[][] a = new int[N+1][M+1];
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= M; j++) {
                a[i][j] = sc.nextInt();
            }
        }
        int[][] dp = new int[N+1][M+1];
        for(int i = 0; i <= N; i++)
            Arrays.fill(dp[i], -1);
        for(int j = 1; j <= M; j++)
            dp[1][j] = a[1][j];
        for(int i = 2; i <= N; i++){
            for(int j = 1; j <= M; j++){
                for(int k = 1; k <= M; k++){
                    if(j == k) continue;
                    dp[i][k] = Math.max(dp[i][k], dp[i-1][j] + a[i][k]);
                }
            }
        }
        int mx = 0;
        for(int i = 1; i <= M; i++)
            mx = Math.max(mx, dp[N][i]);
        System.out.println(mx);
    }
}