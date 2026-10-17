import java.util.*;
import java.io.*;

public class Main {
    static int n, m;
    static List<int[]> graph[];
    static int[] dist, path;
    static final int INF = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        graph = new List[n+1];
        for(int i = 1; i <= n; i++)
            graph[i] = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            graph[u].add(new int[] {v, w});
            graph[v].add(new int[] {u, w});
        }
        st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        dist = new int[n+1];
        Arrays.fill(dist, INF);
        path = new int[n+1];
        dijkstra(a, b);
        System.out.println(dist[b]);
        List<Integer> paths = new ArrayList<>();
        paths.add(b);
        int x = b;
        while(x != a){
            x = path[x];
            paths.add(x);
        }
        Collections.reverse(paths);
        for(int p: paths){
            System.out.print(p+" ");
        }
    }

    static void dijkstra(int src, int dst){
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
                    path[nxt] = now;
                    pq.add(new int[] {nxt, dist[nxt]});
                }
            }
        }
    }
}