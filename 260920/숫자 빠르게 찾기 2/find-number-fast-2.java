import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        TreeSet<Integer> ts = new TreeSet<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++)
            ts.add(Integer.parseInt(st.nextToken()));
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++){
            int x = Integer.parseInt(br.readLine());
            Integer val = ts.ceiling(x);
            if(val == null)
                sb.append(-1);
            else
                sb.append(val);
            sb.append("\n");
        }
        System.out.println(sb);
    }
}