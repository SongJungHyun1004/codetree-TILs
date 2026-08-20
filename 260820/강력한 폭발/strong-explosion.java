import java.util.*;
public class Main {
    static int n, mx;
    static int[][] grid;
    static int[] select;
    static List<int[]> pos = new ArrayList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        grid = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                grid[i][j] = sc.nextInt();
                if(grid[i][j] == 1)
                    pos.add(new int[] {i, j});
            }
        }
        select = new int[pos.size()];
        choose(0);
        System.out.println(mx);
    }

    static void choose(int depth){
        if(depth == pos.size()){
            int cnt = getArea();
            mx = Math.max(mx, cnt);
            return;
        }
        for(int i = 1; i <= 3; i++){
            select[depth] = i;
            choose(depth+1);
        }
    }

    static int getArea(){
        int cnt = 0;
        boolean[][] visited = new boolean[n][n];
        for(int idx = 0; idx < pos.size(); idx++){
            int[] p = pos.get(idx);
            int x = p[0], y = p[1];
            int type = select[idx];
            visited[x][y] = true;
            if(type == 1){
                for(int i = -2; i <=2; i++){
                    int nx = x + i;
                    if(!in_range(nx, y)) continue;
                    visited[nx][y] = true;
                }
            }else if(type == 2){
                int[] dx = {0,1,0,-1};
                int[] dy = {1,0,-1,0};
                for(int i = 0; i < 4; i++){
                    int nx = x + dx[i];
                    int ny = y + dy[i];
                    if(in_range(nx, ny))
                        visited[nx][ny] = true;
                }
            }else if(type == 3){
                int[] dx = {1,1,-1,-1};
                int[] dy = {1,-1,1,-1};
                for(int i = 0; i < 4; i++){
                    int nx = x + dx[i];
                    int ny = y + dy[i];
                    if(in_range(nx, ny))
                        visited[nx][ny] = true;
                }
            }
        }
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(visited[i][j])
                    cnt += 1;
            }
        }
        return cnt;
    }

    static boolean in_range(int x, int y){
        return 0<=x&&x<n && 0<=y&&y<n;
    }

}