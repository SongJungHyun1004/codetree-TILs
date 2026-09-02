import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[][] data = new int[N+1][3];
        for (int i = 1; i <= N; i++) {
            data[i][0] = sc.nextInt();
            data[i][1] = sc.nextInt();
            data[i][2] = sc.nextInt();
        }
        int[][] dp = new int[N+1][3];
        for(int i = 1; i <= N; i++){
            for(int j = 0; j < 3; j++){
                for(int k = 0; k < 3; k++){
                    if(j == k) continue;
                    dp[i][k] = Math.max(dp[i][k], dp[i-1][j] + data[i][k]);
                }
            }
        }
        int mx = 0;
        for(int i = 0; i < 3; i++)
            mx = Math.max(mx, dp[N][i]);
        System.out.println(mx);
    }
}