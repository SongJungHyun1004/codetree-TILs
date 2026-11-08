import java.util.*;

public class Main {
    static int N, M, mx;
    static int[] A;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }
        comb(0, 0, 0);
        System.out.println(mx);
    }

    static void comb(int depth, int idx, int val){
        if(depth == M){
            mx = Math.max(mx, val);
            return;
        }
        if(idx == N)
            return;
        comb(depth+1, idx+1, val^A[idx]);
        comb(depth, idx+1, val);
    }
}