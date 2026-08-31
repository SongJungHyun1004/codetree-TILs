import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        final int offset = 20;
        int[] numbers = new int[N+1];
        for (int i = 1; i <= N; i++) {
            numbers[i] = sc.nextInt();
        }
        long[][] dp = new long[N+1][41];
        dp[0][0+offset] = 1;
        for(int i = 1; i <= N; i++){
            for(int range = -20; range <= 20; range++){
                int j = range + offset;
                int prev = range-numbers[i];
                if(prev >= -20)
                    dp[i][j] += dp[i-1][prev+offset];
                prev = range+numbers[i];
                if(prev <= 20)
                    dp[i][j] += dp[i-1][prev+offset];
            }
        }
        System.out.println(dp[N][M+offset]);
    }

}