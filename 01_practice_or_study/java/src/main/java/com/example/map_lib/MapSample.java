package com.example.map_lib;

import java.util.Map;
import java.util.HashMap;

public class MapSample {
    public static void main(String[] args) throws Exception {
        // ①型定義のジェネリクスは基本データ型ではなくラッパークラスを定義する
        // ★後からTreeMapなどが作れるようにざっくりと親クラスのMap型で定義する
        // ★キーの「fruits」「personf」「category」はString型で、
        // ★値の「"リンゴ"」「"太郎"」「1」は複数の型があるので全ての型を含むObject型（すべての型が入ることが許される）にする必要があるため、Map<String, Object>と定義
        Map<String, Object> exMap = new HashMap<>();
        System.out.println("① 初期化:" + exMap);

        // ②連想配列にキーと値の追加して出力
        exMap.put("fruits", "リンゴ");
        exMap.put("person", "太郎");
        exMap.put("category", 1);
        System.out.println("② 追加:" + exMap);

        // ③連想配列の値を変更して出力
        exMap.replace("fruits", "犬");
        System.out.println("③ 値変更:" + exMap);
        
        // ④連想配列のキーを変更(削除→追加)して出力
        Object beforeValue = exMap.get("fruits");
        exMap.remove("fruits");
        exMap.put("animal", beforeValue);
        System.out.println("④ キー変更:" + exMap);

        // ⑤連想配列の値を取得して出力
        Object result = exMap.get("animal");
        Object result2 = exMap.get("fruits");
        System.out.println("⑤ 値取得(存在):" + result);
        System.out.println("⑤ 値取得(不存在):" + result2);

        // ★⑥連想配列のキーと値をfor文で出力
		for (String key : exMap.keySet()) {
            System.out.println("⑥ -1 キー出力:" + key);
            System.out.println("⑥ -1 値出力:" + exMap.get(key));
        }

        // ⑥連想配列の値をfor文で出力
        for (Object value : exMap.values()) {
            System.out.println("⑥ -2 値出力:" + value);
        }

        // ⑥連想配列のキーと値をfor文で出力
        for (Map.Entry<String, Object> entry : exMap.entrySet()) {
            System.out.println("⑥ -3 キーと値出力:" + entry.getKey() + ":" + entry.getValue());
        }

        // ⑦連想配列のキーを削除して出力
        exMap.remove("animal");
        System.out.println("⑦ animal削除:" + exMap);
        exMap.remove("person");
        System.out.println("⑦ person削除:" + exMap);

        // ⑧連想配列が空か確認(true(////空)/false(空ではない))して出力
        boolean isEmpty = exMap.isEmpty();
        System.out.println("⑧ 中身確認:" + isEmpty);

    }
}
