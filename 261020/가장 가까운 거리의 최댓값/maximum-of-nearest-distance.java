import java.util.*;
import java.io.*;

public class Main {
    static int N, M;
    static List<int[]> graph[];
    static int[] distA, distB, distC;
    static final int INF = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        graph = new List[N+1];
        for(int i = 1; i <= N; i++)
            graph[i] = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            graph[u].add(new int[] {v, d});
            graph[v].add(new int[] {u, d});
        }
        distA = new int[N+1];
        distB = new int[N+1];
        distC = new int[N+1];
        dijkstra(a, distA);
        dijkstra(b, distB);
        dijkstra(c, distC);
        int ans = 0;
        for(int i = 1; i <= N; i++){
            int mn = Math.min(distA[i], Math.min(distB[i], distC[i]));
            ans = Math.max(ans, mn);
        }
        System.out.println(ans);
    }

    static void dijkstra(int src, int[] dist){
        Arrays.fill(dist, INF);
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2)->o1[1]-o2[1]);
        dist[src] = 0;
        pq.add(new int[] {src, 0});
        while(!pq.isEmpty()){
            int[] val = pq.poll();
            int now = val[0], now_d = val[1];
            if(dist[now] < now_d) continue;
            for(int[] nxtVal: graph[now]){
                int nxt = nxtVal[0], nxt_d = nxtVal[1];
                if(dist[nxt] > now_d+nxt_d){
                    dist[nxt] = now_d+nxt_d;
                    pq.add(new int[] {nxt, dist[nxt]});
                }
            }
        }
    }
}