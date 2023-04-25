// 11
// in and diesem fall sollten sie no und nicht yes ausgeben

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
            System.out.println("word: " +word);
            if (Arrays.asList(wordList).contains(word)) {
                System.out.println("Yes");
                // Java自体を終了する。exit語はJavaの実行は続かない
                // System.exit(0);
                // ★そのメソッドを終了する。return後もJavaの実行は続く(基本こっち)
                return;
            }
        }
        System.out.println("No");
        sc.close();
    }
}
