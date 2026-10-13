import java.util.*;
import java.io.*;

public class Main {
    static int n;
    static List<int[]> lines = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            lines.add(new int[] {s, e});
        }
        Collections.sort(lines, (o1, o2)->o1[0]-o2[0]);
        int left = 1;
        int right = 1_000_000_000;
        int ans = left;
        while(left <= right){
            int mid = (left+right)/2;
            if(isPossible(mid)){
                left = mid + 1;
                ans = Math.max(ans, mid);
            } else
                right = mid - 1;
        }
        System.out.println(ans);
    }

    static boolean isPossible(int x){
        int cnt = 0;
        int last = Integer.MIN_VALUE;
        for(int[] line: lines){
            int s = line[0], e = line[1];
            if(last+x <= e){
                cnt += 1;
                last = Math.max(s, last+x);
            }
        }
        return cnt >= n;
    }
}