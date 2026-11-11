import java.util.*;

public class Main {
    static int N, M;
    static int[][] points;
    static int[] select;
    static int mn = Integer.MAX_VALUE;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        points = new int[N][2];
        for (int i = 0; i < N; i++) {
            points[i][0] = sc.nextInt();
            points[i][1] = sc.nextInt();
        }
        select = new int[M];
        choose(0, 0);
        System.out.println(mn);
    }

    static void choose(int depth, int idx){
        if(depth == M){
            int mx = 0;
            for(int i = 0; i < M; i++){
                for(int j = i+1; j < M; j++){
                    int x1 = points[select[i]][0], y1 = points[select[i]][1];
                    int x2 = points[select[j]][0], y2 = points[select[j]][1];
                    int a = Math.abs(x1-x2);
                    int b = Math.abs(y1-y2);
                    int dist = a*a+b*b;
                    mx = Math.max(mx, dist);
                }
            }
            mn = Math.min(mn, mx);
            return;
        }
        if(idx == N)
            return;
        select[depth] = idx;
        choose(depth+1, idx+1);
        choose(depth, idx+1);
    }
}