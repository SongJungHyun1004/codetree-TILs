import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] seq = new int[N+1];
        for (int i = 1; i <= N; i++) {
            seq[i] = sc.nextInt();
        }
        int[][][] dp = new int[N+1][5][M+1];
        for(int i = 0; i <= N; i++){
            for(int j = 0; j <= 4; j++)
                Arrays.fill(dp[i][j], -1);
        }
        for(int i = 1; i <= 4; i++){
            dp[1][i][0] = seq[1] == i ? 1 : 0;
        }
        for(int i = 2; i <= N; i++){
            for(int n1 = 1; n1 <= 4; n1++){
                for(int n2 = 1; n2 <= 4; n2++){
                    int sim = seq[i] == n2 ? 1 : 0;
                    for(int j = 0; j <= M; j++){
                        if(n1 == n2){
                            if(dp[i-1][n1][j] == -1) continue;
                            dp[i][n2][j] = Math.max(dp[i][n2][j], dp[i-1][n1][j] + sim);
                        }
                        else{
                            if(j == 0 || dp[i-1][n1][j-1] == -1) continue;
                            dp[i][n2][j] = Math.max(dp[i][n2][j], dp[i-1][n1][j-1] + sim);
                        }
                    }
                }
            }
        }
        int mx = 0;
        for(int i = 1; i <= 4; i++){
            for(int j = 0; j <= M; j++)
                mx = Math.max(mx, dp[N][i][j]);
        }
        System.out.println(mx);
    }
}