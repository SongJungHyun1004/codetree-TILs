import java.util.*;
public class Main {
    static int N;
    static int[] arr;
    static int mn = Integer.MAX_VALUE;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        choose(0, 0);
        System.out.println(mn != Integer.MAX_VALUE ? mn : -1);
    }

    static void choose(int pos, int jump){
        if(pos == N-1){
            mn = Math.min(mn, jump);
            return;
        }
        for(int d = 1; d <= arr[pos]; d++){
            int nxt = pos + d;
            if(nxt < N){
                choose(nxt, jump+1);
            }
        }
    }
}