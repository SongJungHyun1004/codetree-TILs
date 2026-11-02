import java.util.*;
import java.io.*;

public class Main {
    static int N, M;
    static int[] uf;
    static boolean[] cycle;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        uf = new int[N+1];
        cycle = new boolean[N+1];
        for(int i = 1; i <= N; i++){
            uf[i] = i;
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            if(find(u) != find(v)){
                boolean isCycle = cycle[find(u)] || cycle[find(v)];
                union(u, v);
                cycle[find(u)] = isCycle;
            }else{
                cycle[find(u)] = true;
            }
        }
        int tree = 0;
        Set<Integer> set = new HashSet<>();
        for(int i = 1; i <= N; i++){
            set.add(find(i));
        }
        for(int x: set){
            if(!cycle[x])
                tree += 1;
        }
        System.out.println(tree);
    }

    static int find(int x){
        if(x == uf[x])
            return x;
        return uf[x] = find(uf[x]);
    }

    static void union(int a, int b){
        int x = find(a);
        int y = find(b);
        if(x != y){
            uf[x] = y;
        }
    }
}