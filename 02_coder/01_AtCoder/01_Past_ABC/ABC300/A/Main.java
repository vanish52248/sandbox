import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int A = sc.nextInt();
        int B = sc.nextInt();
        List<Integer> C = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            C.add(sc.nextInt());
        }

        for (int i = 1; i <= N; i++) {
            if ((A+B) == C.get(i-1)) {
                System.out.println(i);
                break;
            }
        }
    }
}
