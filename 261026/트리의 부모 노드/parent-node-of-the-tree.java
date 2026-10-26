import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static List<Integer> tree[];
    static boolean[] visited;
    static int[] par;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        tree = new List[N+1];
        for(int i = 1; i <= N; i++)
            tree[i] = new ArrayList<>();
        for (int i = 1; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            tree[x].add(y);
            tree[y].add(x);
        }
        visited = new boolean[N+1];
        par = new int[N+1];
        par[1] = -1;
        dfs(1);
        StringBuilder sb = new StringBuilder();
        for(int i = 2; i <= N; i++)
            sb.append(par[i]).append("\n");
        System.out.print(sb);
    }

    static void dfs(int x){
        visited[x] = true;
        for(int nx: tree[x]){
            if(!visited[nx]){
                par[nx] = x;
                dfs(nx);
            }
        }
    }
}