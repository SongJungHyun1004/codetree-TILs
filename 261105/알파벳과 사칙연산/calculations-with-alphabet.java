import java.util.*;
public class Main {
    static String expression;
    static int[] var = new int[6];
    static int mx = Integer.MIN_VALUE;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        expression = sc.next();
        comb(0);
        System.out.println(mx);
    }

    static void comb(int depth){
        if(depth == 6){
            mx = Math.max(mx, cal());
            return;
        }
        for(int i = 1; i <= 4; i++){
            var[depth] = i;
            comb(depth + 1);
        }
    }

    static int cal(){
        int res = var[expression.charAt(0)-'a'];
        for(int i = 1; i < expression.length(); i += 2){
            char op = expression.charAt(i);
            int val = var[expression.charAt(i+1)-'a'];
            if(op == '+'){
                res += val;
            }else if(op == '-'){
                res -= val;
            }else if(op == '*'){
                res *= val;
            }
        }
        return res;
    }
}