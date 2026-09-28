import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        TreeSet<int[]> ts = new TreeSet<>((o1, o2)->{
            if(o1[1]==o2[1])
                return o1[0]-o2[0];
            return o1[1]-o2[1];
        });
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int p = Integer.parseInt(st.nextToken());
            int l = Integer.parseInt(st.nextToken());
            ts.add(new int[] {p, l});
        }
        int m = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();
            if (cmd.equals("rc")) {
                int x = Integer.parseInt(st.nextToken());
                if(x == 1)
                    sb.append(ts.last()[0]);
                else if(x == -1)
                    sb.append(ts.first()[0]);
                sb.append("\n");
            } else if (cmd.equals("ad") || cmd.equals("sv")) {
                int p = Integer.parseInt(st.nextToken());
                int l = Integer.parseInt(st.nextToken());
                if(cmd.equals("ad"))
                    ts.add(new int[] {p, l});
                else
                    ts.remove(new int[] {p, l});
            }
        }
        System.out.println(sb);
    }
}