import java.util.*;
import java.io.*;

public class Main {
    static int N, M;
    static List<int[]> graph[];
    static int[] dist;
    static final int INF = Integer.MAX_VALUE;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        graph = new List[N+1];
        for(int i = 1; i <= N; i++)
            graph[i] = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int z = Integer.parseInt(st.nextToken());
            graph[x].add(new int[] {y, z});
            graph[y].add(new int[] {x, z});
        }
        st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        dist = new int[N+1];
        Arrays.fill(dist, INF);
        dijkstra(b);
        sb.append(dist[a]).append("\n");
        int x = a;
        sb.append(x).append(" ");
        while(x != b){
            int nx = INF;
            for(int[] nxtVal: graph[x]){
                int i = nxtVal[0], d = nxtVal[1];
                if(dist[x] == dist[i]+d)
                    nx = Math.min(nx, i);
            }
            x = nx;
            sb.append(x).append(" ");
        }
        System.out.print(sb);
    }

    static void dijkstra(int src){
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
                    dist[nxt] = now_d + nxt_d;
                    pq.add(new int[] {nxt, dist[nxt]});
                }
            }
        }
    }
}