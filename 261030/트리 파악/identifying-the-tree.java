import java.util.*;
import java.io.*;

public class Main {
    static int N, sum;
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
        System.out.println(sum%2 == 1 ? 1 : 0);
    }

    static void dfs(int x, int dist){
        boolean isLeaf = true;
        visited[x] = true;
        for(int nx: tree[x]){
            if(!visited[nx]){
                isLeaf = false;
                dfs(nx, dist+1);
            }
        }
        if(isLeaf)
            sum += dist;
    }
}