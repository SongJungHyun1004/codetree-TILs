import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        Map<Integer, Integer> map = new HashMap<>();
        long ans = 0;
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            ans += map.getOrDefault(k-x, 0);
            map.put(x, map.getOrDefault(x, 0)+1);
        }
        System.out.println(ans);
    }
}