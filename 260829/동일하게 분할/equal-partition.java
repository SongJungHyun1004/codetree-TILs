import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        int total = 0;
        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
            total += arr[i];
        }
        if(total%2 != 0){
            System.out.print("No");
            System.exit(0);
        }
        int s = total/2;
        boolean[] dp = new boolean[s+1];
        dp[0] = true;
        for(int i = 0; i < n; i++){
            for(int j = s; j >= 1; j--){
                if(j >= arr[i] && dp[j-arr[i]])
                    dp[j] = true;
            }
        }
        System.out.print(dp[s/2] ? "Yes" : "No");
    }
}