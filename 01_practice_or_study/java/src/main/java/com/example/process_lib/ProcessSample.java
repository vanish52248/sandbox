// 10
// in diesem fall sollten sie no und nicht yes ausgeben

package com.example.process_lib;

import java.util.*;

public class ProcessSample {
    public static void main(String[] args) {
        // 配列を定義
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
                // 正常終了させるexit
                System.exit(0);
            }
        }
        System.out.println("No");
        sc.close();
    }
}
