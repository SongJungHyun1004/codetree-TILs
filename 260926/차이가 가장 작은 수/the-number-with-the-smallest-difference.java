import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        TreeSet<Integer> ts = new TreeSet<>();
        int ans = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(br.readLine());
            Integer f = ts.floor(x-m);
            Integer c = ts.ceiling(x+m);
            if(f != null){
                ans = Math.min(ans, x-f);
            }
            if(c != null){
                ans = Math.min(ans, c-x);
            }
            ts.add(x);
        }
        System.out.println(ans == Integer.MAX_VALUE ? -1 : ans);
    }
}