import java.util.Scanner;
public class Main {
    static int n, mx;
    static int[][] num, moveDir;
    static int[] dx = {-1,-1,0,1,1,1,0,-1};
    static int[] dy = {0,1,1,1,0,-1,-1,-1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        num = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                num[i][j] = sc.nextInt();
            }
        }
        moveDir = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                moveDir[i][j] = sc.nextInt()-1;
            }
        }
        int r = sc.nextInt()-1;
        int c = sc.nextInt()-1;
        choose(r, c, 0);
        System.out.println(mx);
    }

    static void choose(int x, int y, int dist){
        int val = num[x][y];
        int d = moveDir[x][y];
        mx = Math.max(mx, dist);
        while(true){
            int nx = x + dx[d];
            int ny = y + dy[d];
            if(!in_range(nx, ny))
                break;
            if(val < num[nx][ny])
                choose(nx, ny, dist+1);
            x = nx;
            y = ny;
        }
    }

    static boolean in_range(int x, int y){
        return 0<=x&&x<n && 0<=y&&y<n;
    }

}