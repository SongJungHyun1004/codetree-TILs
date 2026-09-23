import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        TreeSet<Integer> ts = new TreeSet<>();
        ts.add(0);
        StringTokenizer st = new StringTokenizer(br.readLine());
        final int INF = Integer.MAX_VALUE;
        int minDist = INF;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(st.nextToken());
            Integer high = ts.higher(x);
            Integer low = ts.lower(x);
            int d1 = high != null ? high-x : INF;
            int d2 = low != null ? x-low : INF;
            minDist = Math.min(minDist, Math.min(d1, d2));
            sb.append(minDist).append("\n");
            ts.add(x);
        }
        System.out.println(sb);
    }
}