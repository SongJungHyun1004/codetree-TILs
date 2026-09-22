import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        TreeSet<Integer> ts = new TreeSet<>();
        for(int i = 1; i <= m; i++)
            ts.add(i);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            ts.remove(Integer.parseInt(st.nextToken()));
            sb.append(ts.last()).append("\n");
        }
        System.out.println(sb);
    }
}