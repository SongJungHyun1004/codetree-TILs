import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Map<Integer, Integer> pos = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            if(pos.containsKey(x))
                pos.put(x, Math.min(y, pos.get(x)));
            else
                pos.put(x, y);
        }
        long ans = 0;
        for(int x: pos.keySet())
            ans += pos.get(x);
        System.out.println(ans);
    }
}