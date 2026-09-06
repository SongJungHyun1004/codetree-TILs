import java.util.*;
public class Main {
    static int[] dp;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        dp = new int[n+1];
        Arrays.fill(dp, -1);
        System.out.println(bst(n));
    }

    static int bst(int x){
        if(dp[x] != -1) return dp[x];
        if(x <= 1) return 1;
        int cnt = 0;
        for(int i = 0; i < x; i++)
            cnt += bst(i)*bst(x-i-1);
        return dp[x] = cnt;
    }
}