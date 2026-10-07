import java.util.*;
import java.io.*;

public class Main {
    static StringBuilder sb = new StringBuilder();
    static int N, p;
    static int[] S, count;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int Q = Integer.parseInt(br.readLine());
        while(Q-- > 0){
            st = new StringTokenizer(br.readLine());
            int cmd = Integer.parseInt(st.nextToken());
            if(cmd == 1){
                N = Integer.parseInt(st.nextToken());
                S = new int[1101];
                count = new int[3001];
                Arrays.fill(S, -1);
                for(int i = 1; i <= N; i++){
                    S[i] = Integer.parseInt(st.nextToken());
                    count[S[i]] += 1;
                }
                p = N;
            } else if(cmd == 2){
                int v = Integer.parseInt(st.nextToken());
                S[++p] = v;
                count[v] += 1;
            } else if(cmd == 3){
                int idx = Integer.parseInt(st.nextToken());
                if(1 <= idx && idx <= p){
                    int v = S[idx];
                    if(v != -1)
                        count[v] -= 1;
                    sb.append(v).append("\n");
                    S[idx] = -1;
                }else
                    sb.append(-1).append("\n");
            } else if(cmd == 4){
                int K = Integer.parseInt(st.nextToken());
                int[] dp = new int[K+1];
                final int INF = Integer.MAX_VALUE;
                Arrays.fill(dp, INF);
                dp[0] = 0;
                for(int i = 1; i <= K; i++){
                    for(int j = 1; j <= p; j++){
                        if(S[j] == -1) continue;
                        if((i-S[j]) >= 0){
                            if(dp[i-S[j]] == INF) continue;
                            dp[i] = Math.min(dp[i], dp[i-S[j]]+1);
                        }
                    }
                }
                sb.append(dp[K] != INF ? dp[K] : -1).append("\n");
            } else if(cmd == 5){
                int K = Integer.parseInt(st.nextToken());
                int[] suffix = new int[3002];
                for(int i = 3000; i >= 1; i--){
                    suffix[i] = suffix[i+1]+count[i];
                }
                long res = 0;
                for(int i = 1; i <= p; i++){
                    if(S[i] == -1) continue;
                    for(int j = 1; j <= p; j++){
                        if(S[j] == -1) continue;
                        int need = K-S[i]-S[j];
                        if(need < 1)
                            need = 1;
                        res += suffix[need];
                    }
                }
                sb.append(res).append("\n");
            }
        }
        System.out.println(sb);
    }
}