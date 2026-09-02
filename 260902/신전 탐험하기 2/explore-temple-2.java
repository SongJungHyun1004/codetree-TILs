import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] arr = new int[n+1][3];
        for (int i = 1; i <= n; i++) {
            arr[i][0] = sc.nextInt();
            arr[i][1] = sc.nextInt();
            arr[i][2] = sc.nextInt();
        }
        int[][][] dp = new int[n+1][3][3];
        dp[1][0][0] = arr[1][0];
        dp[1][1][1] = arr[1][1];
        dp[1][2][2] = arr[1][2];
        for(int i = 2; i <= n; i++){
            for(int j = 0; j < 3; j++){
                for(int k = 0; k < 3; k++){
                    if(j == k) continue;
                    for(int l = 0; l < 3; l++){
                        if(i == n && k == l) continue;
                        dp[i][k][l] = Math.max(dp[i][k][l], dp[i-1][j][l]+arr[i][k]);
                    }
                }
            }
        }
        int mx = 0;
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++)
                mx = Math.max(mx, dp[n][i][j]);
        }
        System.out.println(mx);
    }
}