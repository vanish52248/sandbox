import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String S = sc.next();
        char S1 = S.charAt(0);
        boolean isCorrect = true;
        for (int i = 1; i < S.length(); i++) {
            if (S.charAt(i) != S1) {
                S1 = S.charAt(i);
                isCorrect = true;
            } else {
                isCorrect = false;
                break;
            }
        }
        System.out.println(isCorrect ? "Yes" : "No");
    }
}
