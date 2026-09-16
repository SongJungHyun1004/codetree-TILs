import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            String word = sc.next();
            char[] arr = word.toCharArray();
            Arrays.sort(arr);
            String key = new String(arr);
            map.put(key, map.getOrDefault(key, 0)+1);
        }
        List<String> keySet =  new ArrayList<>(map.keySet());
        Collections.sort(keySet, (o1, o2) -> map.get(o2)-map.get(o1));
        System.out.println(map.get(keySet.get(0)));
    }
}