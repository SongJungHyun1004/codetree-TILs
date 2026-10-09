import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        long left = 1;
        long right = 10_000_000_000L;
        long ans = right;
        while(left <= right){
            long mid = (left+right)/2;
            if(count(mid) >= n){
                right = mid - 1;
                ans = Math.min(ans, mid);
            }else{
                left = mid + 1;
            }
        }
        System.out.println(ans);
    }

    static long count(long x){
        long cnt = x/3+x/5-x/15;
        return x-cnt;
    }

}