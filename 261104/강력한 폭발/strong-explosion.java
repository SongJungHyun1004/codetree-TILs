import java.util.*;
public class Main {
    static int n, M, mx;
    static int[] select;
    static List<int[]> pos = new ArrayList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        int[][] grid = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                grid[i][j] = sc.nextInt();
                if(grid[i][j] == 1){
                    pos.add(new int[] {i, j});
                }
            }
        }
        M = pos.size();
        select = new int[M];
        choose(0);
        System.out.println(mx);
    }

    static void choose(int depth){
        if(depth == M){
            mx = Math.max(mx, explodedCell(select));
            return;
        }
        for(int i = 1; i <= 3; i++){
            select[depth] = i;
            choose(depth+1);
        }
    }

    static int explodedCell(int[] select){
        boolean[][] exp = new boolean[n][n];
        int cnt = 0;
        for(int i = 0; i < M; i++){
            int[] p = pos.get(i);
            int x = p[0], y = p[1];
            int type = select[i];
            exp[x][y] = true;
            if(type == 1){
                int[] dx = new int[] {-1,-2,1,2};
                int[] dy = new int[] {0,0,0,0};
                for(int j = 0; j < 4; j++){
                    int nx = x + dx[j];
                    int ny = y + dy[j];
                    if(in_range(nx, ny))
                        exp[nx][ny] = true;
                }
            }else if(type == 2){
                int[] dx = new int[] {0,1,0,-1};
                int[] dy = new int[] {1,0,-1,0};
                for(int j = 0; j < 4; j++){
                    int nx = x + dx[j];
                    int ny = y + dy[j];
                    if(in_range(nx, ny))
                        exp[nx][ny] = true;
                }
            }else if(type == 3){
                int[] dx = new int[] {1,1,-1,-1};
                int[] dy = new int[] {1,-1,1,-1};
                for(int j = 0; j < 4; j++){
                    int nx = x + dx[j];
                    int ny = y + dy[j];
                    if(in_range(nx, ny))
                        exp[nx][ny] = true;
                }
            }
        }
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(exp[i][j])
                    cnt += 1;
            }
        }
        return cnt;
    }

    static boolean in_range(int x, int y){
        return 0<=x&&x<n && 0<=y&&y<n;
    }
}