import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long s = sc.nextLong();
        long left = 1;
        long right = (long)Math.sqrt(s*2)+1;
        long ans = 1;
        while(left <= right){
            long mid = (left+right)/2;
            if(mid*(mid+1)/2 <= s){
                left = mid + 1;
                ans = Math.max(ans, mid);
            }else{
                right = mid-1;
            }
        }
        System.out.println(ans);
    }
}