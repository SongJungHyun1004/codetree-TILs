import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[] points = new int[n];
        for (int i = 0; i < n; i++) {
            points[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(points);
        int left = 1;
        int right = 1_000_000_000;
        int ans = left;
        while(left <= right){
            int mid = (left+right)/2;
            if(count(points, n, mid) >= m){
                left = mid + 1;
                ans = Math.max(ans, mid);
            }else{
                right = mid - 1;
            }
        }
        System.out.println(ans);
    }

    static int count(int[] points, int n, int dist){
        int pre = points[0];
        int cnt = 1;
        for(int i = 1; i < n; i++){
            if(points[i] - pre >= dist){
                cnt += 1;
                pre = points[i];
            }
        }
        return cnt;
    }

}