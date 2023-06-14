import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Long A = sc.nextLong();
        Long B = sc.nextLong();

        System.out.println((A+B-1) / B);
        sc.close();
    }
}
