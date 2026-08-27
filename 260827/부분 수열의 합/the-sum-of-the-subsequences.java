import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr = new int[n];
        boolean[] dp = new boolean[m+1];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        dp[0] = true;
        for(int i = 0; i < n; i++){
            for(int j = m; j >= 1; j--){
                if(j >= arr[i] && dp[j-arr[i]]){
                    dp[j] = true;
                }
            }
        }
        System.out.print(dp[m] ? "Yes" : "No");
    }
}