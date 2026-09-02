import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        String s = sc.next();
        int[][][] dp = new int[N+1][2][K+1];
        for(int i = 0; i <= N; i++){
            for(int j = 0; j < 2; j++)
                Arrays.fill(dp[i][j], -1);
        }
        dp[0][0][0] = 0;
        for(int i = 1; i <= N; i++){
            for(int j = 0; j < 2; j++){
                for(int k = 0; k < 2; k++){
                    if(j == k){
                        for(int l = 0; l <= K; l++){
                            if(dp[i-1][j][l] == -1) continue;
                            if(s.charAt(i-1) == 'L')
                                dp[i][k][l] = Math.max(dp[i][k][l], dp[i-1][j][l] + (k == 0 ? 1 : 0));
                            else
                                dp[i][k][l] = Math.max(dp[i][k][l], dp[i-1][j][l] + (k == 1 ? 1 : 0));
                        }
                    }else{
                        for(int l = 1; l <= K; l++){
                            if(dp[i-1][j][l-1] == -1) continue;
                            if(s.charAt(i-1) == 'L')
                                dp[i][k][l] = Math.max(dp[i][k][l], dp[i-1][j][l-1] + (k == 0 ? 1 : 0));
                            else
                                dp[i][k][l] = Math.max(dp[i][k][l], dp[i-1][j][l-1] + (k == 1 ? 1 : 0));
                        }
                    }
                }
            }
        }
        int mx = 0;
        for(int i = 0; i <= K; i++){
            mx = Math.max(mx, Math.max(dp[N][0][i], dp[N][1][i]));
        }
        System.out.println(mx);
    }
}