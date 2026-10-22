import java.util.*;
import java.io.*;

public class Main {
    static int N, M;
    static List<int[]> graph[];
    static int[] dist1, dist2;
    static final int INF = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int red1 = Integer.parseInt(st.nextToken());
        int red2 = Integer.parseInt(st.nextToken());
        graph = new List[N+1];
        for(int i = 1; i <= N; i++)
            graph[i] = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            graph[u].add(new int[] {v, w});
            graph[v].add(new int[] {u, w});
        }
        dist1 = new int[N+1];
        dist2 = new int[N+1];
        dijkstra(red1, dist1);
        dijkstra(red2, dist2);

        int mn = INF;
        for(int i = 1; i <= N; i++){
            if(i == red1 || i == red2) continue;
            if(dist1[i] == INF || dist2[i] == INF) continue;
            if(dist1[red2] != INF)
                mn = Math.min(mn, dist1[i]+dist1[red2]+dist2[i]);
            if(dist2[red1] != INF)
                mn = Math.min(mn, dist2[i]+dist2[red1]+dist1[i]);
        }
        System.out.println(mn != INF ? mn : -1);
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