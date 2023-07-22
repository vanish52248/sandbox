import java.util.*;

class  Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        String S = sc.next();
        String T = sc.next();


        Boolean isCorrect = true;
        for (int i = 0; i < N; i++) {
            if (S.charAt(i) == T.charAt(i)) {
                continue;
            } else if (S.charAt(i) == '1' && T.charAt(i) == 'l') {
                continue;
            } else if (T.charAt(i) == '1' && S.charAt(i) == 'l') {
                continue;
            } else if (S.charAt(i) == 'o' && T.charAt(i) == '0') {
                continue;
            } else if (T.charAt(i) == 'o' && S.charAt(i) == '0') {
                continue;
            } else {
                isCorrect = false;
                break;
            }
        }

        System.out.println(isCorrect ? "Yes" : "No");
    }
}
