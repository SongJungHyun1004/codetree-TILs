import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                String end;
                if(j == N)
                    end = "";
                else
                    end = ", ";
                System.out.print(i + " * " + j + " = " + (i * j) + end);
            }
            System.out.println();
        }
    }
}
