import java.util.*;
import java.io.*;

public class Main {
    static int n, m;
    static long[][] points;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        points = new long[m][2];
        long left = 0;
        long right = 0;
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            long s = Long.parseLong(st.nextToken());
            long e = Long.parseLong(st.nextToken());
            points[i] = new long[] {s, e};
            right = Math.max(right, e);
        }
        Arrays.sort(points, (o1, o2) -> Long.compare(o1[0], o2[0]));
        long ans = left;
        while(left <= right){
            long mid = (left+right)/2;
            if(isPossible(mid)){
                left = mid + 1;
                ans = Math.max(ans, mid);
            }else{
                right = mid - 1;
            }
        }
        System.out.println(ans);
    }

    static boolean isPossible(long x){
        int cnt = 0;
        long last = -1;
        for(int i = 0; i < m; i++){
            long s = points[i][0];
            long e = points[i][1];
            long p = s;
            if(cnt > 0)
                p = Math.max(s, last + x);
            while(p <= e){
                last = p;
                p += x;
                cnt += 1;
            }
        }

        return cnt >= n;
    }
}