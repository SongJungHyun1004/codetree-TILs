import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        TreeSet<int[]> ts = new TreeSet<>((o1, o2) -> {
            if(o1[0] == o2[0])
                return o1[1]-o2[1];
            return o1[0]-o2[0];
        });
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            ts.add(new int[]{x, y});
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            int qx = sc.nextInt();
            int qy = sc.nextInt();
            int[] val = ts.ceiling(new int[] {qx, qy});
            if(val == null)
                sb.append(-1).append(' ').append(-1);
            else
                sb.append(val[0]).append(' ').append(val[1]);
            sb.append("\n");
        }
        System.out.println(sb);
    }
}