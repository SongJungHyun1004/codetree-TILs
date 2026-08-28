import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        int total = 0;
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
            total += arr[i];
        }
        int s = total/2;
        boolean[] dp = new boolean[s+1];
        dp[0] = true;
        for(int i = 0; i < n; i++){
            for(int j = s; j >= 1; j--){
                if(j >= arr[i] && dp[j-arr[i]]){
                    dp[j] = true;
                }
            }
        }
        for(int i = s; i >= 1; i--){
            if(dp[i]){
                System.out.println(Math.abs((total-i)-i));
                break;
            }
        }
    }
}