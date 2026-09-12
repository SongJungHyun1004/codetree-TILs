import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] numbers = new int[N+1];
        for (int i = 1; i <= N; i++) {
            numbers[i] = sc.nextInt();
        }
        long[][] dp = new long[N+1][41];
        final int offset = 20;
        dp[0][0+offset] = 1;
        for(int i = 1; i <= N; i++){
            for(int val = -20; val <= 20; val++){
                int j = val+offset;
                if(j-numbers[i] >= 0)
                    dp[i][j] += dp[i-1][j-numbers[i]];
                if(j+numbers[i] <= 40)
                    dp[i][j] += dp[i-1][j+numbers[i]];
            }
        }
        System.out.println(dp[N][M+offset]);
    }
}