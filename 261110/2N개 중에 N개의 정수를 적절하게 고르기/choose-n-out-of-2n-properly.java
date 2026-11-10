import java.util.*;
public class Main {
    static int N, total;
    static int mn = Integer.MAX_VALUE;
    static int[] arr;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        arr = new int[2 * N];
        for (int i = 0; i < 2 * N; i++) {
            arr[i] = sc.nextInt();
            total += arr[i];
        }
        choose(0, 0, 0);
        System.out.println(mn);
    }

    static void choose(int depth, int idx, int sum){
        if(depth == N){
            mn = Math.min(mn, Math.abs(sum-(total-sum)));
            return;
        }
        if(idx == 2*N)
            return;
        choose(depth+1, idx+1, sum+arr[idx]);
        choose(depth, idx+1, sum);
    }
}