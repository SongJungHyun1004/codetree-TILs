import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] arr = new int[n];
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
            map.put(arr[i], map.getOrDefault(arr[i], 0)+1);
        }
        int cnt = 0;
        for(int i = 0; i < n; i++){
            map.put(arr[i], map.get(arr[i])-1);
            for(int j = 0; j < i; j++){
                int target = k-arr[i]-arr[j];
                cnt += map.getOrDefault(target, 0);
            }
        }
        System.out.println(cnt);
    }
}