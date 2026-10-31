import java.util.*;

public class Main {
    static int N, K, leaf;
    static Map<Integer, List<Integer>> tree = new HashMap<>();
    static Map<Integer, Integer> par = new HashMap<>();
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        K = sc.nextInt();
        int[] arr = new int[N];
        arr[0] = sc.nextInt();
        int root = arr[0];
        int p = -1;
        for (int i = 1; i < N; i++) {
            arr[i] = sc.nextInt();
            if(arr[i] - arr[i-1] > 1){
                int val = arr[++p];
                par.put(arr[i], val);
                tree.computeIfAbsent(val, k -> new ArrayList<>()).add(arr[i]);
            }
            else{
                par.put(arr[i], arr[p]);
                tree.computeIfAbsent(arr[p], k -> new ArrayList<>()).add(arr[i]);
            }
        }
        if (par.get(K) == null || par.get(par.get(K)) == null) {
            System.out.println(0);
            return;
        }
        int parent = par.get(K);
        int grand = par.get(parent);
        for (int sibling : tree.getOrDefault(grand, new ArrayList<>())) {
            if (sibling == parent) continue;
            leaf += tree.getOrDefault(sibling, new ArrayList<>()).size();
        }
        System.out.println(leaf);
    }

}