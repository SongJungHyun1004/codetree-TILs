import java.util.*;
public class Main {
    static StringBuilder sb = new StringBuilder();
    static int k, n;
    static int[] select;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        k = sc.nextInt();
        n = sc.nextInt();
        select = new int[n];
        choose(0);
        System.out.print(sb);
    }

    static void choose(int depth){
        if(depth == n){
            for(int i = 0; i < n; i++){
                sb.append(select[i]).append(" ");
            }
            sb.append("\n");
            return;
        }
        for(int i = 1; i <= k; i++){
            if(depth > 1 && select[depth-1] == i && select[depth-2] == i)
                continue;
            select[depth] = i;
            choose(depth+1);
        }
    }
}
