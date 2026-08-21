import java.util.*;

public class Main {
    static int n;
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
        for(int x = n; x >= 1; x--){
            comb(0, 0, x);
        }
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

    static void comb(int start, int depth, int target){
        if(depth == target){
            if(isPossible()){
                System.out.println(target);
                System.exit(0);
            }
            return;
        }
        for(int i = start; i < n; i++){
            list.add(segments[i]);
            comb(i+1, depth+1, target);
            list.remove(list.size()-1);
        }
    }
}