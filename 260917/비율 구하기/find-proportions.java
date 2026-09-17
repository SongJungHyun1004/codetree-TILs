import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Map<String, Integer> counter = new TreeMap<>();
        for (int i = 0; i < n; i++) {
            String word = sc.next();
            counter.put(word, counter.getOrDefault(word, 0)+1);
        }
        for(String word: counter.keySet()){
            double val = counter.get(word)*100/(double)n;
            System.out.println(String.format("%s %.4f", word, val));
        }
    }
}