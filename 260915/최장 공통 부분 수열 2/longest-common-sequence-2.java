import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String b = sc.next();
        int n = a.length();
        int m = b.length();
        a = " "+a;
        b = " "+b;
        int[][] dp = new int[n+1][m+1];
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= m; j++){
                if(a.charAt(i) == b.charAt(j))
                    dp[i][j] = dp[i-1][j-1]+1;
                else
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
            }
        }
        StringBuilder sb = new StringBuilder();
        int i = n, j = m;
        while(i > 0 && j > 0){
            if(a.charAt(i) == b.charAt(j)){
                sb.append(a.charAt(i));
                i -= 1;
                j -= 1;
            }
            else{
                if(dp[i-1][j] > dp[i][j-1])
                    i -= 1;
                else
                    j -= 1;
            }
        }
        System.out.println(sb.reverse().toString());
    }
}