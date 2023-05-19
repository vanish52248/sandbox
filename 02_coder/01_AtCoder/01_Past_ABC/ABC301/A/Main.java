import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String S = sc.next();
        int aCount = 0;
        int tCount = 0;
        String turn = "";
        for (int i = 0; i < N; i++) {
            char c = S.charAt(i);
            if (c == 'A') {
                aCount ++;
                if (turn.equals("") && aCount == N / 2) {
                    turn = "A";
                }
            } else if (c == 'T') {
                tCount ++;
                if (turn.equals("") && tCount == N / 2) {
                    turn = "T";
                }

            }
        }
        
        if (aCount > tCount) {
            System.out.println("A");
        } else if (aCount < tCount) {
            System.out.println("T");
        } else {
            if (turn == "T") {
                System.out.println("T");
            } else {
                System.out.println("A");
            }
        }
        sc.close();
    }
}
