import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        for(int t = 0; t < T; t++){
            TreeSet<Integer> ts = new TreeSet<>();
            int K = Integer.parseInt(br.readLine());
            for(int i = 0; i < K; i++){
                StringTokenizer st = new StringTokenizer(br.readLine());
                char cmd = st.nextToken().charAt(0);
                int x = Integer.parseInt(st.nextToken());
                if(cmd == 'I'){
                    ts.add(x);
                }else if(cmd == 'D' && !ts.isEmpty()){
                    if(x == 1){
                        ts.remove(ts.last());
                    }else if(x == -1){
                        ts.remove(ts.first());
                    }
                }
            }
            if(ts.isEmpty())
                sb.append("EMPTY\n");
            else
                sb.append(ts.last()).append(" ").append(ts.first()).append("\n");
        }
        System.out.println(sb);
    }
}