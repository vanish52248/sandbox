import java.util.*;

class Main {
    public static void main(String[] args) {
        String[] wordList = {"and", "not", "that", "the", "you"};
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String[] wordArray = new String[N];
        for(int i = 0; i < N; i++) {
            wordArray[i] = sc.next();
        }

        for (String word: wordArray) {
            if (Arrays.asList(wordList).contains(word)) {
                System.out.println("Yes");
                System.exit(0);
            }
        }
        System.out.println("No");
    }
}
