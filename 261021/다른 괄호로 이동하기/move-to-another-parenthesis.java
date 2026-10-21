import java.util.*;
import java.io.*;

public class Main {
    static int N, A, B;
    static char[][] grid;
    static int[][] dist;
    static final int INF = Integer.MAX_VALUE;
    static int[] dx = {0,1,0,-1};
    static int[] dy = {1,0,-1,0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());
        grid = new char[N][N];
        for (int i = 0; i < N; i++) {
            String input = br.readLine();
            for (int j = 0; j < N; j++) {
                grid[i][j] = input.charAt(j);
            }
        }
        dist = new int[N][N];
        int mx = 0;
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                dijkstra(i, j);
                for(int x = 0; x < N; x++){
                    for(int y = 0; y < N; y++){
                        if(dist[x][y] == INF) continue;
                        mx = Math.max(mx, dist[x][y]);
                    }
                }
            }
        }
        System.out.println(mx);
    }

    static void dijkstra(int sx, int sy){
        for(int i = 0; i < N; i++)
            Arrays.fill(dist[i], INF);
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2)->o1[2]-o2[2]);
        dist[sx][sy] = 0;
        pq.add(new int[] {sx, sy, 0});
        while(!pq.isEmpty()){
            int[] val = pq.poll();
            int x = val[0], y = val[1], d = val[2];
            if(dist[x][y] < d) continue;
            for(int i = 0; i < 4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                if(in_range(nx, ny)){
                    int nd = 0;
                    if(grid[x][y] != grid[nx][ny])
                        nd = B;
                    else
                        nd = A;
                    if(dist[nx][ny] > d + nd){
                        dist[nx][ny] = d + nd;
                        pq.add(new int[] {nx, ny, dist[nx][ny]});
                    }
                }
            }
        }
    }

    static boolean in_range(int x, int y){
        return 0<=x&&x<N && 0<=y&&y<N;
    }
}