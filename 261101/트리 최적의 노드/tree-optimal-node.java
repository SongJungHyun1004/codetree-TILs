import java.util.*;
import java.io.*;

public class Main {
    static int N, mx, mx_node;
    static List<Integer> tree[];
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        tree = new List[N+1];
        for(int i = 1; i <= N; i++)
            tree[i] = new ArrayList<>();
        for (int i = 0; i < N - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            tree[u].add(v);
            tree[v].add(u);
        }
        visited = new boolean[N+1];
        dfs(1, 0);
        visited = new boolean[N+1];
        dfs(mx_node, 0);
        System.out.println((mx%2)==0 ? mx/2 : (mx+1)/2);
    }

    static void dfs(int x, int dist) {
        visited[x] = true;
        if(dist > mx){
            mx = dist;
            mx_node = x;
        }
        for(int nx: tree[x]){
            if(!visited[nx]){
                dfs(nx, dist+1);
            }
        }
    }
}