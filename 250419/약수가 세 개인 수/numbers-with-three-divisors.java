import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int start = sc.nextInt();
        int end = sc.nextInt();
        int cnt = 0;
        for(int i=start; i<=end; i++){
            int tmp = 0;
            for(int j=1; j<=i; j++){
                if(i%j == 0)
                    tmp += 1;
            }
            if(tmp == 3)
                cnt += 1;
        }
        System.out.print(cnt);
    }
}