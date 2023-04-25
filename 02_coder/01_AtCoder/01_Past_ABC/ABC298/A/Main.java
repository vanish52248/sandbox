import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String s = sc.next();
        List<Character> l = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            char t = s.charAt(i);
            if (s.contains("x")) {
                System.out.println("No");
                return;
            }
            l.add(t);
        }
        if (l.contains('o')) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}
