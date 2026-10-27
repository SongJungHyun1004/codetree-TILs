import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static List<int[]> tree[];
    static boolean[] visited;
    static int mx, mx_node;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        tree = new List[N+1];
        for(int i = 1; i <= N; i++)
            tree[i] = new ArrayList<>();
        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            tree[u].add(new int[] {v, w});
            tree[v].add(new int[] {u, w});
        }
        visited = new boolean[N+1];
        dfs(1, 0);
        visited = new boolean[N+1];
        dfs(mx_node, 0);
        System.out.println(mx);
    }

    static void dfs(int x, int dist){
        if(mx < dist){
            mx = dist;
            mx_node = x;
        }
        visited[x] = true;
        for(int[] nxtVal: tree[x]){
            int nx = nxtVal[0], nd = nxtVal[1];
            if(!visited[nx])
                dfs(nx, dist+nd);
        }
    }
}