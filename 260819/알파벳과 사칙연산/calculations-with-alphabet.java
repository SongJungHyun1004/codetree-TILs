import java.io.*;

public class Main {
    static String expr;
    static int[] val = new int[6];
    static int maxResult = Integer.MIN_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        expr = br.readLine();
        findMax(0);

        System.out.println(maxResult);
    }

    static void findMax(int depth) {
        if (depth == 6) {
            maxResult = Math.max(maxResult, calculate());
            return;
        }

        for (int i = 1; i <= 4; i++) {
            val[depth] = i;
            findMax(depth + 1);
        }
    }

    static int calculate() {
        int res = val[expr.charAt(0) - 'a'];
        for (int i = 1; i < expr.length(); i += 2) {
            char op = expr.charAt(i);
            int nextVal = val[expr.charAt(i + 1) - 'a'];
            if (op == '+') {
                res += nextVal;
            } else if (op == '-') {
                res -= nextVal;
            } else if (op == '*') {
                res *= nextVal;
            }
        }
        return res;
    }
}