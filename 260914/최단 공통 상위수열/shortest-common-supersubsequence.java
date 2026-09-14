import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = " "+sc.next();
        String t = " "+sc.next();
        int n = s.length()-1;
        int m = t.length()-1;
        int[][] dp = new int[n+1][m+1];
        dp[1][1] = s.charAt(1) == t.charAt(1) ? 1 : 2;
        for(int i = 2; i <= n; i++){
            if(s.charAt(i) == t.charAt(1))
                dp[i][1] = i;
            else
                dp[i][1] = dp[i-1][1]+1;
        }
        for(int j = 2; j <= m; j++){
            if(s.charAt(1) == t.charAt(j))
                dp[1][j] = j;
            else
                dp[1][j] = dp[1][j-1]+1;
        }
        for(int i = 2; i <= n; i++){
            for(int j = 2; j <= m; j++){
                if(s.charAt(i) == t.charAt(j)){
                    dp[i][j] = dp[i-1][j-1] + 1;
                }else{
                    dp[i][j] = Math.min(dp[i-1][j], dp[i][j-1])+1;
                }
            }
        }
        System.out.println(dp[n][m]);
    }
}