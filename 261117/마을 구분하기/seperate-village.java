import java.util.*;

public class Main {
    static int n, sz;
    static int[][] grid;
    static boolean[][] visited;
    static int[] dx = {0,1,0,-1};
    static int[] dy = {1,0,-1,0};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        grid = new int[n][n];
        visited = new boolean[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                grid[i][j] = sc.nextInt();
        List<Integer> list = new ArrayList<>();                
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] == 1 && !visited[i][j]){
                    sz = 0;
                    dfs(i, j);
                    list.add(sz);
                }
            }
        }
        Collections.sort(list);
        System.out.println(list.size());
        for(int i = 0; i < list.size(); i++)
            System.out.println(list.get(i));
    }

    static void dfs(int x, int y){
        visited[x][y] = true;
        sz += 1;
        for(int i = 0; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(in_range(nx, ny) && grid[nx][ny] == 1 && !visited[nx][ny])
                dfs(nx, ny);
        }
    }

    static boolean in_range(int x, int y){
        return 0<=x&&x<n && 0<=y&&y<n;
    }
}