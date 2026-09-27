import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        TreeSet<int[]> ts = new TreeSet<>((o1, o2) -> {
            if(o1[0] == o2[0])
                return o1[1]-o2[1];
            return o1[0]-o2[0];
        });
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        for(int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            ts.add(new int[] {x, y});
        }
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < m; i++){
            int k = Integer.parseInt(br.readLine());
            int[] p = ts.ceiling(new int[] {k, -1});
            if(p == null)
                sb.append(-1).append(" ").append(-1);
            else{
                sb.append(p[0]).append(" ").append(p[1]);
                ts.remove(p);
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}