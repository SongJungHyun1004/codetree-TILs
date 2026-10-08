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
        arr = new int[n];
        int left = 1;
        int right = 0;
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
            right = Math.max(right, arr[i]);
        }
        int ans = 0;
        while(left <= right){
            int mid = (left+right)/2;
            if(isPossible(mid)){
                left = mid + 1;
                ans = Math.max(ans, mid);
            }else
                right = mid - 1;
        }
        System.out.println(ans);
    }

    static boolean isPossible(int mod){
        int cnt = 0;
        for(int i = 0; i < n; i++){
            cnt += arr[i]/mod;
        }
        return cnt >= m;
    }
}