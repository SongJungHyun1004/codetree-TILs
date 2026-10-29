import java.util.*;
import java.io.*;

public class Main {
    static int M;
    static Map<Integer, Integer> indegree = new HashMap<>();
    static Set<Integer> node = new HashSet<>();
    static Map<Integer, List<Integer>> graph = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            indegree.put(b, indegree.getOrDefault(b, 0) + 1);
            node.add(a);
            node.add(b);
            graph.putIfAbsent(a, new ArrayList<>());
            graph.get(a).add(b);
        }

        int root = -1;
        int rootCnt = 0;
        for (int x : node) {
            int degree = indegree.getOrDefault(x, 0);
            if (degree == 0) {
                root = x;
                rootCnt++;
            } else if (degree > 1) {
                System.out.println(0);
                return;
            }
        }

        if (rootCnt != 1) {
            System.out.println(0);
            return;
        }

        Queue<Integer> q = new LinkedList<>();
        Set<Integer> visited = new HashSet<>();
        q.add(root);
        visited.add(root);

        while (!q.isEmpty()) {
            int cur = q.poll();
            for (int next : graph.getOrDefault(cur, Collections.emptyList())) {
                if (visited.add(next)) {
                    q.add(next);
                }
            }
        }

        System.out.println(visited.size() == node.size() ? 1 : 0);
    }
}