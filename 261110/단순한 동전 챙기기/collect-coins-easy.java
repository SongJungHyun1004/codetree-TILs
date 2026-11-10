import java.util.*;

public class Main {
    static int N, sx, sy, ex, ey;
    static int mn = Integer.MAX_VALUE;
    static char[][] grid;
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};
    static int[] select = new int[3];
    static List<int[]> pos = new ArrayList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        grid = new char[N][N];
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
        for(int num = 1; num <= 9; num++){
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if((grid[i][j]-'0') == num)
                        pos.add(new int[] {i, j});
                }
            }
        }
        choose(0, 0);
        System.out.println(mn != Integer.MAX_VALUE ? mn : -1);
    }

    static void choose(int depth, int idx) {
        if(depth == 3) {
            mn = Math.min(mn, cal());
            return;
        }
        if(idx == pos.size())
            return;
        select[depth] = idx;
        choose(depth+1, idx+1);
        choose(depth, idx+1);
    }

    static int cal(){
        int res = 0;
        int px = sx, py = sy;
        for(int i = 0; i < 3; i++){
            int[] val = pos.get(select[i]);
            int x = val[0], y = val[1];
            res += getDist(px, py, x, y);
            px = x;
            py = y;
        }
        res += getDist(px, py, ex, ey);
        return res;
    }

    static int getDist(int x1, int y1, int x2, int y2){
        return Math.abs(x1-x2)+Math.abs(y1-y2);
    }

    static boolean in_range(int x, int y) {
        return 0 <= x && x < N && 0 <= y && y < N;
    }
}
