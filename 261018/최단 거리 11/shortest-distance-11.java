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
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int z = Integer.parseInt(st.nextToken());
            graph[x].add(new int[] {y, z});
            graph[y].add(new int[] {x, z});
        }
        dist = new int[n+1];
        path = new int[n+1];
        Arrays.fill(dist, INF);
        st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        dijkstra(b, a);
        System.out.println(dist[a]);
        int x = a;
        System.out.print(x+" ");
        while(x != b){
            int nxt = Integer.MAX_VALUE;
            for(int[] val: graph[x]){
                int i = val[0], d = val[1];
                if(dist[x] == dist[i] + d)
                    nxt = Math.min(nxt, i);
            }
            x = nxt;
            System.out.print(x+" ");
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
            for(int[] nxtVal : graph[now]){
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