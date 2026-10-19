import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static List<int[]> graph[];
    static long[][] dist;
    static final long INF = Long.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        
        int[][] minCost = new int[1001][1001];
        int[][] minTime = new int[1001][1001];
        for(int i = 1; i <= 1000; i++){
            Arrays.fill(minCost[i], Integer.MAX_VALUE);
            Arrays.fill(minTime[i], Integer.MAX_VALUE);
        }

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int cost = Integer.parseInt(st.nextToken());
            int stopCount = Integer.parseInt(st.nextToken());
            int[] station = new int[stopCount];
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < stopCount; j++) {
                station[j] = Integer.parseInt(st.nextToken());
            }
            for (int a = 0; a < stopCount; a++) {
                for(int b = a+1; b < stopCount; b++){
                    int u = station[a];
                    int v = station[b];
                    int time = b - a;
                    if (minCost[u][v] > cost || (minCost[u][v] == cost && minTime[u][v] > time)) {
                        minCost[u][v] = cost;
                        minTime[u][v] = time;
                    }
                }
            }
        }

        graph = new List[1001];
        for(int i = 1; i <= 1000; i++)
            graph[i] = new ArrayList<>();

        for(int u = 1; u <= 1000; u++){
            for(int v = 1; v <= 1000; v++){
                if(minCost[u][v] != Integer.MAX_VALUE){
                    graph[u].add(new int[] {v, minCost[u][v], minTime[u][v]});
                }
            }
        }

        dist = new long[1001][2];
        for(int i = 1; i <= 1000; i++)
            Arrays.fill(dist[i], INF);
        dijkstra(A, B);
        long[] ans = dist[B];
        System.out.println((ans[0] != INF ? ans[0]:-1 )+" "+(ans[1] != INF ? ans[1]:-1));
    }

    static void dijkstra(int src, int dst){
        PriorityQueue<long[]> pq = new PriorityQueue<>((o1, o2)->{
            if(o1[1]==o2[1])
                return Long.compare(o1[2], o2[2]);
            return Long.compare(o1[1], o2[1]);
        });
        dist[src] = new long[] {0, 0};
        pq.add(new long[] {src, 0, 0});
        while(!pq.isEmpty()){
            long[] val = pq.poll();
            int now = (int) val[0];
            long now_c = val[1], now_t = val[2];
            if(dist[now][0] < now_c) continue;
            if(dist[now][0] == now_c && dist[now][1] < now_t) continue;
            for(int[] nxtVal : graph[now]){
                int nxt = nxtVal[0];
                long nxt_c = nxtVal[1], nxt_t = nxtVal[2];
                if(dist[nxt][0] > now_c+nxt_c){
                    dist[nxt] = new long[] {now_c+nxt_c, now_t+nxt_t};
                    pq.add(new long[] {nxt, now_c+nxt_c, now_t+nxt_t});
                }
                if(dist[nxt][0] == now_c+nxt_c && dist[nxt][1] > now_t+nxt_t){
                    dist[nxt] = new long[] {now_c+nxt_c, now_t+nxt_t};
                    pq.add(new long[] {nxt, now_c+nxt_c, now_t+nxt_t});
                }
            }
        }
    }
}