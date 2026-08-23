import java.util.*;
public class Main {
    static int n, mn;
    static int[] arr;
    static List<Integer> list = new ArrayList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        mn = n;
        choose(0);
        System.out.println(mn != n ? mn : -1);
    }

    static void choose(int depth){
        if(depth == n-1){
            mn = Math.min(mn, list.size());
            return;
        }
        for(int i = 1; i <= arr[depth]; i++){
            if(depth+i < n){
                list.add(depth+i);
                choose(depth+i);
                list.remove(list.size()-1);
            }
        }
    }
}