import java.util.*;

public class Main {
    static int N, M;
    static int[] select;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        select = new int[M];
        comb(0, 1);
        System.out.println(sb);
    }

    static void comb(int depth, int num){
        if(depth == M){
            for(int i = 0; i < M; i++)
                sb.append(select[i]).append(" ");
            sb.append("\n");
            return;
        }
        if(num > N)
            return;
        select[depth] = num;
        comb(depth+1, num+1);
        comb(depth, num+1);
    }
}