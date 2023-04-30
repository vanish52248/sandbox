import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // abc と受け取る場合は[a, b, c]とリストで一文字ずつ格納される
        String[] S = sc.nextLine().split("");
        String[] S2 = S.clone();

        for (int i = 0; i < S.length; i += 2) {
            S[i+1] = S2[i];
            S[i] = S2[i+1];
        }
        System.out.println(String.join("", S));
    }   
}
