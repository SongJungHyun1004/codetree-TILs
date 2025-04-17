import java.util.*;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        char a = sc.next().charAt(0);
        String[] words = {"apple", "banana", "grape", "blueberry", "orange"};
        int cnt = 0;
        for(String word : words){
            if(word.charAt(2) == a || word.charAt(3) == a){
                System.out.println(word);
                cnt += 1;
            }
        }
        System.out.print(cnt);
    }
}