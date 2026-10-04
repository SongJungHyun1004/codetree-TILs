import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[] arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            int x = Integer.parseInt(br.readLine());
            sb.append(upper(arr, x)-lower(arr, x)).append("\n");
        }
        System.out.println(sb);
    }

    static int lower(int[] arr, int x){
        int left = 0;
        int right = arr.length-1;
        int res = arr.length;
        while(left <= right){
            int mid = (left+right)/2;
            if(arr[mid] >= x){
                right = mid - 1;
                res = Math.min(res, mid);
            }
            else{
                left = mid + 1;
            }
        }
        return res;
    }

    static int upper(int[] arr, int x){
        int left = 0;
        int right = arr.length-1;
        int res = arr.length;
        while(left <= right){
            int mid = (left+right)/2;
            if(arr[mid] > x){
                right = mid - 1;
                res = Math.min(res, mid);
            }
            else{
                left = mid + 1;
            }
        }
        return res;
    }
}