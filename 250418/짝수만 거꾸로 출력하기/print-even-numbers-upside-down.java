import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<Integer> list = new ArrayList<>();
        for(int i =0; i<n; i++){
            int num = sc.nextInt();
            if(num%2==0)
                list.add(num);
        }
        Collections.reverse(list);
        for(int x : list)
            System.out.print(x+" ");
    }
}