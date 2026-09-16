import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] A = new int[n];
        int[] B = new int[n];
        int[] C = new int[n];
        int[] D = new int[n];
        for (int i = 0; i < n; i++) {
            A[i] = sc.nextInt();
        }
        for (int i = 0; i < n; i++) {
            B[i] = sc.nextInt();
        }
        for (int i = 0; i < n; i++) {
            C[i] = sc.nextInt();
        }
        for (int i = 0; i < n; i++) {
            D[i] = sc.nextInt();
        }
        Map<Integer, Integer> group1 = new HashMap<>();
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                int val = A[i]+B[j];
                group1.put(val, group1.getOrDefault(val, 0)+1);
            }
        }
        long ans = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                int target = -C[i]-D[j];
                ans += group1.getOrDefault(target, 0);
            }
        }
        System.out.println(ans);
    }
}