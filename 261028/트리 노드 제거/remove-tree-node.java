import java.util.*;

public class Main {
    static int N, leaf;
    static int[] parent;
    static List<Integer> tree[];
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        parent = new int[N];
        tree = new List[N];
        int root = -1;
        for(int i = 0; i < N; i++)
            tree[i] = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            int x = sc.nextInt();
            parent[i] = x;
            if(x != -1)
                tree[x].add(i);
            else
                root = i;
        }
        int deleteNode = sc.nextInt();
        parent[deleteNode] = -2;
        dfs(root);
        System.out.println(leaf);
    }

    static void dfs(int x){
        if(parent[x] == -2)
            return;
        boolean isLeaf = true;
        for(int nx: tree[x]){
            if(parent[nx] == -2) continue;
            isLeaf = false;
            dfs(nx);
        }
        if(isLeaf)
            leaf += 1;
    }
}