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
        }
        int cnt = 0;
        for(int i = 0; i < n; i++){
            for(int j = i+1; j < n; j++){
                int target = k-arr[i]-arr[j];
                cnt += map.getOrDefault(target, 0);
            }
            map.put(arr[i], map.getOrDefault(arr[i], 0)+1);
        }
        System.out.println(cnt);
    }
}