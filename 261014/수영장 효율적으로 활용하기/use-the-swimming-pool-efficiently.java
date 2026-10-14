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
        st = new StringTokenizer(br.readLine());
        int left = 1;
        int right = 0;
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            left = Math.max(left, arr[i]);
            right += arr[i];
        }
        int ans = right;
        while(left <= right){
            int mid = (left+right)/2;
            if(isPossible(mid)){
                right = mid - 1;
                ans = Math.min(ans, mid);
            }else
                left = mid + 1;
        }
        System.out.println(ans);
    }

    static boolean isPossible(int time){
        int lane = 1;
        int sum = 0;
        for(int i = 0; i < n; i++){
            if(sum+arr[i] <= time){
                sum += arr[i];
            }else{
                sum = arr[i];
                lane += 1;
            }
        }
        return lane <= m;
    }
}