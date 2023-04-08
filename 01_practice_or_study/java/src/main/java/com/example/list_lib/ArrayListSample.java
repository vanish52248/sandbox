package com.example.list_lib;

import java.util.*;

public class ArrayListSample {
    public static void main(String[] args) {
        // ①型定義のジェネリクスは基本データ型ではなくラッパークラスを定義する
        // ②★LinkedListなど後から作れるようにざっくりと親クラスのList型で定義する
        List<Integer> points = new ArrayList<>();

        points.add(10);
        points.add(80);
        points.add(75);

        // 1番目に要素を挿入
        points.add(1, 22);
        // 1番目の要素を変更
        points.set(1, 99);

        // 2番目の要素を特定取得
        System.out.println("2番目の要素は:" + points.get(2));

        // 2番目の要素を削除
        points.remove(2);

        // 配列要素数のカウント
        System.out.println("全体の要素数は:" + points.size());

        // 一覧取得 方法①(for文)
        for (int i = 0; i < points.size(); i++) {
            System.out.println("一覧取得① の要素は:" + points.get(i));
        }
        System.out.println();

        // 一覧取得 方法②(拡張for文)
        for (int i: points) {
            System.out.println("一覧取得② の要素は:" + i);
        }
        System.out.println();

        // ★一覧取得 方法③(Collectionクラスのみに使用できるイテレータ)
        Iterator<Integer> it = points.iterator();
        // 要素がある限りtrueとしてループする
        while (it.hasNext()) {
            int e = it.next();
            System.out.println("一覧取得③ の要素は" + e);
        }

        // 存在確認とインデックス確認
        if (points.contains(10)) {
            System.out.println("pointsの中に10が含まれている");
            System.out.println(points.indexOf(10) + "番目に10が存在する");
        }
        System.out.println();

        // 配列型を定義
        String[] wordList = {"and", "not", "that", "the", "you"};
        // 配列型をList型に変換する Arrays.asList() を使用することで contains()が使用できるので存在判定を行う
        if (Arrays.asList(wordList).contains("and")) {
            System.out.println("wordListの中に'and'が含まれている。");
        }

        // 全ての要素を削除
        points.clear();

        // 要素数が0か確認
        if (points.isEmpty()) {
            System.out.println("pointsの要素数が0個である");
        }
    }
}
