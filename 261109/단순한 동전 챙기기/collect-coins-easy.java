import java.util.*;

public class Main {
    static int N, sx, sy, ex, ey;
    static int mn = Integer.MAX_VALUE;
    static char[][] grid;
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};
    static int[][][][] minMove;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        grid = new char[N][N];
        minMove = new int[N][N][10][10];
        for (int i = 0; i < N; i++) {
            for (int r = 0; r < N; r++) {
                for (int c = 0; c < 10; c++) {
                    for (int d = 0; d < 10; d++) {
                        minMove[i][r][c][d] = Integer.MAX_VALUE;
                    }
                }
            }
        }

        for (int i = 0; i < N; i++) {
            String str = sc.next();
            for (int j = 0; j < N; j++) {
                grid[i][j] = str.charAt(j);
                if (grid[i][j] == 'S') {
                    sx = i;
                    sy = j;
                } else if (grid[i][j] == 'E') {
                    ex = i;
                    ey = j;
                }
            }
        }
        
        choose(sx, sy, 0, 0, 0);
        System.out.println(mn != Integer.MAX_VALUE ? mn : -1);
    }

    static void choose(int x, int y, int pre, int cnt, int move) {
        if (move >= mn) return;
        if (minMove[x][y][cnt][pre] <= move) return;
        minMove[x][y][cnt][pre] = move;
        if (x == ex && y == ey && cnt >= 3) {
            mn = Math.min(mn, move);
            return;
        }

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if (in_range(nx, ny)) {
                choose(nx, ny, pre, cnt, move + 1);
                if (Character.isDigit(grid[nx][ny])) {
                    int val = grid[nx][ny] - '0';
                    if (val > pre) {
                        choose(nx, ny, val, cnt + 1, move + 1);
                    }
                }
            }
        }
    }

    static boolean in_range(int x, int y) {
        return 0 <= x && x < N && 0 <= y && y < N;
    }
}