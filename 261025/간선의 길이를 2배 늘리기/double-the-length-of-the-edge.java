import java.util.*;
import java.io.*;

public class Main {
    static int N, M;
    static int[][] graph;
    static int[] dist;
    static final int INF = Integer.MAX_VALUE;
    static List<int[]> edges = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        graph = new int[N+1][N+1];
        for(int i = 1; i <= N; i++){
            Arrays.fill(graph[i], INF);
            graph[i][i] = 0;
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            graph[u][v] = w;
            graph[v][u] = w;
            edges.add(new int[] {u, v, w});
        }
        dist = new int[N+1];
        dijkstra();
        int before = dist[N];
        int mx = 0;
        for(int[] edge: edges){
            int u = edge[0], v = edge[1], w = edge[2];
            graph[u][v] = 2*w;
            graph[v][u] = 2*w;
            dijkstra();
            int after = dist[N];
            mx = Math.max(mx, after);
            graph[u][v] = w;
            graph[v][u] = w;
        }
        System.out.println(mx-before);
    }

    static void dijkstra(){
        Arrays.fill(dist, INF);
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2)->o1[1]-o2[1]);
        dist[1] = 0;
        pq.add(new int[] {1, 0});
        while(!pq.isEmpty()){
            int[] val = pq.poll();
            int now = val[0], now_d = val[1];
            if(dist[now] < now_d) continue;
            for(int nxt = 1; nxt <= N; nxt++){
                int nxt_d = graph[now][nxt];
                if(nxt_d == INF) continue;
                if(dist[nxt] > now_d + nxt_d){
                    dist[nxt] = now_d + nxt_d;
                    pq.add(new int[] {nxt, dist[nxt]});
                }
            }
        }
    }
}