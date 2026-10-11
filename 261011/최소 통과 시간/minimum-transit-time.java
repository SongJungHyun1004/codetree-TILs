import java.util.*;
import java.io.*;

public class Main {
    static int n, m;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[m];
        for (int i = 0; i < m; i++)
            arr[i] = Integer.parseInt(br.readLine());
        long left = 1;
        long right = 1_000_000_000L*n;
        long ans = right;
        while(left <= right){
            long mid = (left+right)/2;
            if(isPossible(mid)){
                right = mid - 1;
                ans = Math.min(ans, mid);
            }else
                left = mid + 1;
        }
        System.out.println(ans);
    }

    static boolean isPossible(long x){
        long cnt = 0;
        for(int i = 0; i < m; i++){
            cnt += x/arr[i];
        }
        return cnt >= n;
    }
}