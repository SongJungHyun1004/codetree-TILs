import java.util.*;
public class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String ans = "";
        for(int i = 0; i < s.length(); i++){
            if(i == 1 || i == s.length()-2)
                ans += 'a';
            else
                ans += s.charAt(i);
        }
        System.out.print(ans);
    }
}