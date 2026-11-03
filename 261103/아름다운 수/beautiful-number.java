import java.util.Scanner;
public class Main {
    static int N, cnt;
    static int[] select;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        select = new int[N];
        choose(0);
        System.out.println(cnt);
    }

    static void choose(int depth){
        if(depth == N){
            if(isBeauty(select))
                cnt += 1;
            return;
        }
        for(int i = 1; i <= 4; i++){
            select[depth] = i;
            choose(depth+1);
        }
    }

    static boolean isBeauty(int[] select){
        int i = 0;
        while(i < N){
            if(i + select[i]-1 >= N)
                return false;
            for(int j = 0; j < select[i]; j++){
                if(select[i] != select[i+j])
                    return false;
            }
            i += select[i];
        }
        return true;
    }
}