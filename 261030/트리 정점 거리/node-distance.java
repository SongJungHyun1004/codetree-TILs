import java.util.*;

public class Main {
    static int N, M;
    static List<int[]> tree[];
    static boolean[] visited;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        tree = new List[N+1];
        for(int i = 1; i <= N; i++)
            tree[i] = new ArrayList<>();
        for (int i = 0; i < N - 1; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int d = sc.nextInt();
            tree[u].add(new int[]{v, d});
            tree[v].add(new int[]{u, d});
        }
        for (int i = 0; i < M; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            visited = new boolean[N+1];
            System.out.println(dfs(u, v, 0));
        }
    }

    static int dfs(int x, int dst, int dist){
        visited[x] = true;
        if(x == dst)
            return dist;
        for(int[] nxtVal: tree[x]){
            int nx = nxtVal[0], nd = nxtVal[1];
            if(visited[nx]) continue;
            int res = dfs(nx, dst, dist+nd);
            if(res != -1)
                return res;
        }
        return -1;
    }
}