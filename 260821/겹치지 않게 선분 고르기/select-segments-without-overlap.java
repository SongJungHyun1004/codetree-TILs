import java.util.*;

public class Main {
    static int n, ans;
    static int[][] segments;
    static List<int[]> list = new ArrayList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        segments = new int[n][2];
        for (int i = 0; i < n; i++) {
            segments[i][0] = sc.nextInt();
            segments[i][1] = sc.nextInt();
        }
        choose(0);
        System.out.println(ans);
    }

    static boolean isOverlapped(int[] seg1, int[] seg2){
        int s1 = seg1[0], e1 = seg1[1];
        int s2 = seg2[0], e2 = seg2[1];
        return (s1 <= s2 && s2 <= e1) || (s1 <= e2 && e2 <= e1)
        || (s2 <= s1 && s1 <= e2) || (s2 <= e1 && e1 <= e2);
    }

    static boolean isPossible(){
        for(int i = 0; i < list.size(); i++){
            for(int j = i+1; j < list.size(); j++){
                if(isOverlapped(list.get(i), list.get(j)))
                    return false;
            }
        }
        return true;
    }

    static void choose(int idx){
        if(idx == n){
            if(isPossible())
                ans = Math.max(ans, list.size());
            return;
        }
        int[] val = new int[] {segments[idx][0], segments[idx][1]};
        list.add(val);
        choose(idx+1);
        list.remove(list.size()-1);
        choose(idx+1);
    }
}