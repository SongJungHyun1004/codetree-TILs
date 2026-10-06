import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long m = Long.parseLong(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        long a = Long.parseLong(st.nextToken());
        long b = Long.parseLong(st.nextToken());
        long mn = Long.MAX_VALUE;
        long mx = Long.MIN_VALUE;
        for(long t = a; t <= b; t++){
            long res = binarySearch(t, m);
            mn = Math.min(mn, res);
            mx = Math.max(mx, res);
        }
        System.out.println(mn+" "+mx);
    }

    static long binarySearch(long t, long m){
        long left = 1;
        long right = m;
        long cnt = 1;
        while(left <= right){
            long mid = (left+right)/2;
            if(mid == t)
                return cnt;
            if(mid > t)
                right = mid - 1;
            else
                left = mid + 1;
            cnt += 1;
        }
        return cnt;
    }
}