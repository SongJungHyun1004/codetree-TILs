import java.util.*;

public class Main {
    static int N, M, K;
    static int[][] grid, temper;
    static Turtle[] ts;
    static Volcano[] vs;
    static boolean[] exploded;
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};

    static class Turtle {
        int x, y;
        int time = -1;
        int state;
        Turtle(int x, int y, int time, int state){
            this.x = x;
            this.y = y;
            this.time = time;
            this.state = state;
        }
    }

    static class Volcano {
        int x, y;
        int p;
        int max;
        Volcano(int x, int y, int p, int max){
            this.x = x;
            this.y = y;
            this.p = p;
            this.max = max;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        K = sc.nextInt();
        grid = new int[N][N];
        temper = new int[N][N];
        ts = new Turtle[M+1];
        vs = new Volcano[K];
        exploded = new boolean[K];
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                grid[i][j] = sc.nextInt();
                if(grid[i][j] == 1)
                    grid[i][j] = -1;
            }
        }
        for(int id = 1; id <= M; id++){
            int x = sc.nextInt();
            int y = sc.nextInt();
            ts[id] = new Turtle(x, y, -1, 0);
            grid[x][y] = id;
        }
        for(int i = 0; i < K; i++){
            int x = sc.nextInt();
            int y = sc.nextInt();
            int max = sc.nextInt();
            vs[i] = new Volcano(x, y, 0, max);
        }

        for(int turn = 1; turn <= 100; turn++){
            move(turn);
            charge();
            eruption();
            reset();
        }
        for(int i = 1; i <= M; i++)
            System.out.println(ts[i].time);
    }

    static void move(int turn){
        for(int id = 1; id <= M; id++){
            if(ts[id].state == 0){
                bfs(id, turn);
            }
        }
    }

    static void bfs(int id, int turn){
        Queue<int[]> q = new LinkedList<>();
        boolean[][] visited = new boolean[N][N];
        q.add(new int[] {ts[id].x, ts[id].y, -1});
        while(!q.isEmpty()){
            int[] val = q.poll();
            int x = val[0], y = val[1], dir = val[2];
            if(x == N-1 && y == N-1){
                grid[ts[id].x][ts[id].y] = 0;
                ts[id].x += dx[dir];
                ts[id].y += dy[dir];
                if(ts[id].x == N-1 && ts[id].y == N-1){
                    ts[id].time = turn;
                    ts[id].state = 1;
                }else{
                    grid[ts[id].x][ts[id].y] = id;
                }
                return;
            }
            for(int i = 0; i < 4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                if(in_range(nx, ny) && !visited[nx][ny] && grid[nx][ny] == 0){
                    visited[nx][ny] = true;
                    int nd = dir == -1 ? i : dir;
                    q.add(new int[] {nx, ny, nd});
                }
            }
        }
    }

    static boolean in_range(int x, int y){
        return 0<=x&&x<N && 0<=y&&y<N;
    }

    static void charge(){
        for(int i = 0; i < K; i++){
            vs[i].p += 10;
        }
    }
    
    static void eruption(){
        exploded = new boolean[K];
        for(int i = 0; i < K; i++){
            if(vs[i].p >= vs[i].max){
                exploded[i] = true;
                spread(vs[i].x, vs[i].y, vs[i].max);
            }
        }

        while(true){
            boolean isNew = false;
            for(int i = 0; i < K; i++){
                if(!exploded[i]){
                    Volcano v = vs[i];
                    if(v.p + temper[v.x][v.y] >= v.max){
                        exploded[i] = true;
                        isNew = true;
                        spread(v.x, v.y, v.max);
                    }
                }
            }
            if(!isNew)
                break;
        }

        for(int id = 1; id <= M; id++){
            if(ts[id].state == 0 && temper[ts[id].x][ts[id].y] >= 20)
                ts[id].state = 2;
        }
    }

    static void spread(int x, int y, int t){
        temper[x][y] += t;
        for(int i = 0; i < 4; i++){
            int nx = x;
            int ny = y;
            int nt = t;
            while(true){
                nx += dx[i];
                ny += dy[i];
                nt /= 2;
                if(!in_range(nx, ny) || grid[nx][ny] == -1 || nt == 0)
                    break;
                temper[nx][ny] += nt;
            }
        }
    }

    static void reset(){
        temper = new int[N][N];
        for(int i = 0; i < K; i++){
            if(exploded[i]){
                vs[i].p = 0;
            }
        }
        exploded = new boolean[K];
    }
}