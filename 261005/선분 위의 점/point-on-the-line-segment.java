import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[] points = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            points[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(points);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int l = Integer.parseInt(st.nextToken());
            int r = Integer.parseInt(st.nextToken());
            sb.append(upper(points, r)-lower(points, l)).append("\n");
        }
        System.out.println(sb);
    }

    static int lower(int[] points, int x){
        int left = 0;
        int right = points.length-1;
        int res = points.length;
        while(left <= right){
            int mid = (left+right)/2;
            if(points[mid] >= x){
                right = mid - 1;
                res = Math.min(res, mid);
            }else
                left = mid + 1;
        }
        return res;
    }

    static int upper(int[] points, int x){
        int left = 0;
        int right = points.length-1;
        int res = points.length;
        while(left <= right){
            int mid = (left+right)/2;
            if(points[mid] > x){
                right = mid - 1;
                res = Math.min(res, mid);
            }else
                left = mid + 1;
        }
        return res;
    }
}