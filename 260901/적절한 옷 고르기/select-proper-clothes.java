import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] s = new int[n+1];
        int[] e = new int[n+1];
        int[] v = new int[n+1];
        for (int i = 1; i <= n; i++) {
            s[i] = sc.nextInt();
            e[i] = sc.nextInt();
            v[i] = sc.nextInt();
        }
        int[][] dp = new int[m+1][n+1];
        for(int i = 1; i <= n; i++){
            if(!(s[i] <= 1 && 1 <= e[i])) continue;
            for(int j = 1; j <= n; j++){
                if(!(s[j] <= 2 && 2 <= e[j])) continue;
                dp[2][j] = Math.max(dp[2][j], Math.abs(v[i]-v[j]));
            }
        }
        for(int i = 3; i <= m; i++){
            for(int j = 1; j <= n; j++){
                if(!(s[j] <= i-1 && i-1 <= e[j])) continue;
                for(int k = 1; k <= n; k++){
                    if(!(s[k] <= i && i <= e[k])) continue;
                    dp[i][k] = Math.max(dp[i][k], dp[i-1][j]+Math.abs(v[j]-v[k]));
                }
            }
        }
        int mx = 0;
        for(int i = 1; i <= n; i++)
            mx = Math.max(mx, dp[m][i]);
        System.out.println(mx);
    }
}