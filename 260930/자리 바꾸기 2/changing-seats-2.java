import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[] a = new int[k];
        int[] b = new int[k];
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            a[i] = Integer.parseInt(st.nextToken());
            b[i] = Integer.parseInt(st.nextToken());
        }
        int[] pos = new int[n+1];
        Set<Integer>[] visited = new HashSet[n+1];
        for(int i = 1; i <= n; i++){
            pos[i] = i;
            visited[i] = new HashSet<>();
            visited[i].add(i);
        }
        for(int round = 0; round < 3; round++){
            for(int i = 0; i < k; i++){
                int p1 = pos[a[i]];
                int p2 = pos[b[i]];
                visited[p1].add(b[i]);
                visited[p2].add(a[i]);
                pos[a[i]] = p2;
                pos[b[i]] = p1;
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            sb.append(visited[i].size()).append("\n");
        }
        System.out.print(sb);
    }
}