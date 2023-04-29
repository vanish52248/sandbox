import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String S = sc.next();
        
        int count = 0;
        for (int i = 0; i < N; i++) {
            char c = S.charAt(i);
            if (c == '|') {
                count ++;
                if (count == 2) {
                    break;
                }
            } else if (count == 1 && c == '*') {
                System.out.println("in");
                return;
            }
        }
        System.out.println("out");
    }
}
