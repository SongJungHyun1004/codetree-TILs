import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] segments = new int[n][2];
        int[] dp = new int[n];
        Arrays.fill(dp, -1);
        for (int i = 0; i < n; i++) {
            segments[i][0] = sc.nextInt();
            segments[i][1] = sc.nextInt();
        }
        Arrays.sort(segments, (o1, o2) -> {
            if(o1[1] == o2[1])
                return o1[0]-o2[0];
            return o1[1]-o2[1];
        });
        dp[0] = 1;
        for(int i = 1; i < n; i++){
            for(int j = 0; j < i; j++){
                if(dp[j] == -1) continue;
                if(segments[j][1] < segments[i][0])
                    dp[i] = Math.max(dp[i], dp[j]+1);
            }
        }
        int mx = 0;
        for(int i = 0; i < n; i++)
            mx = Math.max(mx, dp[i]);
        System.out.println(mx);
    }
}