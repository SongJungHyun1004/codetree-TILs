import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        long k = sc.nextLong();
        long left = 1;
        long right = n*n;
        long ans = right;
        while(left <= right){
            long mid = (left+right)/2;
            if(count(mid, n) >= k){
                right = mid - 1;
                ans = Math.min(ans, mid);
            }else{
                left = mid + 1;
            }
        }
        System.out.println(ans);
    }

    static long count(long x, long n){
        long cnt = 0;
        for(int i = 1; i <= n; i++)
            cnt += Math.min(n, x/i);
        return cnt;
    }

}