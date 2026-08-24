import java.util.*;
public class Main {
    static int[] dp;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        dp = new int[n+1];
        Arrays.fill(dp, -1);
        System.out.println(getBST(n));
    }

    static int getBST(int x){
        if(dp[x] != -1)
            return dp[x];
        if(x <= 1)
            return 1;
        int cnt = 0;
        for(int i = 0; i < x; i++){
            cnt += getBST(i)*getBST(x-i-1);
        }
        return dp[x] = cnt;
    }
}