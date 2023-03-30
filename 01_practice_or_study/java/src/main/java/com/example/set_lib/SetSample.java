package com.example.set_lib;

import java.util.HashSet;
import java.util.Set;
import java.util.TreeSet;

public class SetSample {
    public static void main(String[] args) {
        // ①型定義のジェネリクスは基本データ型ではなくラッパークラスを定義する
        // ②★後からTreeSetなどが作れるようにざっくりと親クラスのSet型で定義する
        Set<String> colors = new HashSet<>();

        colors.add("赤");
        colors.add("青");
        colors.add("黄");
        colors.add("赤");

        System.out.println("色は合計" + colors.size() + "種類");

        // 順序は保証されていないので毎回変わる
        for (String color: colors) {
            System.out.println("一覧取得：" + color);
        }

        Set<String> words = new TreeSet<>();
        words.add("wolf");
        words.add("dog");
        words.add("cat");
        words.add("dog");
        words.add("panda");

        // 順序が保証されているので毎回一定
        for (String word: words) {
            System.out.println("一覧取得：" + word);
        }
    }
}
