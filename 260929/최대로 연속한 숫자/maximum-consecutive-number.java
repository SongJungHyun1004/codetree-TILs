import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        TreeSet<Integer> removed = new TreeSet<>();
        removed.add(-1);
        removed.add(n+1);
        TreeSet<int[]> ts = new TreeSet<>((o1, o2) -> {
            if(o2[2]==o1[2])
                return o1[0]-o2[0];
            return o2[2]-o1[2];
        });
        ts.add(new int[] {-1, n+1, n+1});
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            int x = Integer.parseInt(st.nextToken());
            int left = removed.lower(x);
            int right = removed.higher(x);
            ts.remove(new int[]{left, right, right-left-1});
            ts.add(new int[] {left, x, x-left-1});
            ts.add(new int[] {x, right, right-x-1});
            removed.add(x);
            sb.append(ts.first()[2]).append("\n");
        }
        System.out.println(sb);
    }
}