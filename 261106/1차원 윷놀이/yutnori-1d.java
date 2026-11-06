import java.util.*;
public class Main {
    static int N, M, K, mx;
    static int[] nums, select, move;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        K = sc.nextInt();
        nums = new int[N];
        select = new int[N];
        move = new int[K+1];
        for (int i = 0; i < N; i++) {
            nums[i] = sc.nextInt();
        }
        choose(0);
        System.out.println(mx);
    }

    static void choose(int depth){
        if(depth == N){
            Arrays.fill(move, 1);
            for(int i = 0; i < N; i++) {
                move[select[i]] += nums[i];
            }
            int score = 0;
            for(int i = 1; i <= K; i++){
                if(move[i] >= M)
                    score += 1;
            }
            mx = Math.max(mx, score);
            return;
        }
        for(int i = 1; i <= K; i++){
            select[depth] = i;
            choose(depth + 1);
        }
    }
}