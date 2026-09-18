import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        TreeMap<Integer, Integer> numbers = new TreeMap<>();
        for (int i = 1; i <= n; i++) {
            int x = sc.nextInt();
            if(!numbers.containsKey(x))
                numbers.put(x, i);
        }
        numbers.forEach((k, v) -> {
            System.out.println(k+" "+v);
        });
    }
}