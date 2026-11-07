import java.util.*;
public class Main {
    static int N, mx;
    static int[][] num, dir;
    static int[] dx = {0,-1,-1,0,1,1,1,0,-1};
    static int[] dy = {0,0,1,1,1,0,-1,-1,-1};


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        num = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                num[i][j] = sc.nextInt();
            }
        }
        dir = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                dir[i][j] = sc.nextInt();
            }
        }
        int r = sc.nextInt()-1;
        int c = sc.nextInt()-1;
        dfs(r, c, 0);
        System.out.println(mx);
    }

    static void dfs(int x, int y, int move){
        mx = Math.max(mx, move);
        int d = dir[x][y];
        for(int i = 1; i < N; i++){
            int nx = x + dx[d]*i;
            int ny = y + dy[d]*i;
            if(in_range(nx, ny) && num[nx][ny] > num[x][y]){
                dfs(nx, ny, move+1);
            }
        }
    }

    static boolean in_range(int x, int y){
        return 0<=x&&x<N && 0<=y&&y<N;
    }
}