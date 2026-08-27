import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] info = new int[n+1][3];
        int[] dp = new int[n+1];
        Arrays.fill(dp, -1);
        for (int i = 1; i <= n; i++) {
            info[i][0] = sc.nextInt();
            info[i][1] = sc.nextInt();
            info[i][2] = sc.nextInt();
        }
        Arrays.sort(info, (o1, o2)->{
            if(o1[1]==o2[1])
                return o1[0]-o2[0];
            return o1[1]-o2[1];
        });
        dp[0] = 0;
        for(int i = 1; i <= n; i++){
            for(int j = 0; j < i; j++){
                if(dp[j] == -1) continue;
                if(info[j][1] < info[i][0]){
                    dp[i] = Math.max(dp[i], dp[j]+info[i][2]);
                }
            }
        }
        int mx = 0;
        for(int i = 1; i <= n; i++)
            mx = Math.max(mx, dp[i]);
        System.out.println(mx);
    }
}