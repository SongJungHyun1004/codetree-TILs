import java.util.Scanner;
public class Main {
    static int N, cnt;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        choose(0);
        System.out.println(cnt);
    }

    static void choose(int n){
        if(n == N){
            cnt += 1;
            return;
        }
        for(int i = 1; i <= 4; i++){
            if(n + i <= N){
                choose(n+i);
            }
        }
    }
}