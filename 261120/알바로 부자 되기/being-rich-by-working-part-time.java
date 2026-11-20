import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] s = new int[n+1];
        int[] e = new int[n+1];
        int[] p = new int[n+1];
        for (int i = 1; i <= n; i++) {
            s[i] = sc.nextInt();
            e[i] = sc.nextInt();
            p[i] = sc.nextInt();
        }
        int[] dp = new int[n+1];
        Arrays.fill(dp, -1);
        dp[0] = 0;
        for(int i = 1; i <= n; i++){
            for(int j = 0; j < i; j++){
                if(dp[j] == -1) continue;
                if(s[i] > e[j]){
                    dp[i] = Math.max(dp[i], dp[j]+p[i]);
                }
            }
        }
        int mx = 0;
        for(int i = 1; i <= n; i++)
            mx = Math.max(mx, dp[i]);
        System.out.println(mx);
    }
}