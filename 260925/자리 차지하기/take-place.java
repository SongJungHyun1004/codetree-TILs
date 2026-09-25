import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        TreeSet<Integer> ts = new TreeSet<>();
        for(int i = 1; i <= n; i++)
            ts.add(i);
        st = new StringTokenizer(br.readLine());
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(st.nextToken());
            Integer target = ts.floor(x);
            if(target == null) break;
            ts.remove(target);
            ans += 1;
        }
        System.out.println(ans);
    }
}