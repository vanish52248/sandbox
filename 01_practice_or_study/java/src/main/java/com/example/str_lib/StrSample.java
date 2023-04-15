package com.example.str_lib;

class Valid {
    boolean isValidPlayerName(String name) {
        /*
         * 正規表現でのバリデーションメソッド
         * . => 任意の位置文字
         * * => 直前の文字の⓪回以上の繰り返し
         * {} => 指定回数の繰り返し
         * [] => いずれかの文字
         * [a-z] => 範囲内いずれかの文字
         * ^ => 文字列の先頭
         * $ => 文字列の末尾
         */
        return name.matches("[A-Z][A-Z0-9]{7}");
    }
}

public class StrSample {    
    public static void main(String[] args) {
        String name = "A0123456";
        String s1 = "スッキリJava";
        String s2 = "Java";
        String s3 = "java";
        String s4 = "";
        String s5 = "Java and JavaScript";
        String s6 = "Java programming";
        String s7 = "abcDEF";
        String s8  = " a b c ";
        String s9 = "a1b1c2d2e1";
        String s10 = "abc,def:ghi";
        String s11 = "ABCDEFGHIJKLMNOP";

        if (s2.equals(s3)) {
            System.out.println("s2とs3は等しい");
        }

        if (s2.equalsIgnoreCase(s3)) {
            System.out.println("S2とS3はケースを区別しなければ等しい");
        }

        System.out.println("s1の長さは" + s1.length() + "です");

        if (s4.isEmpty()) {
            System.out.println("s4は空文字です");
        }

        if (s5.contains("Java")) {
            System.out.println("文字列s5は、Javaを含んでいます。");
        }

        if (s5.endsWith("Java")) {
            System.out.println("文字列s5はJavaが末尾にあります。");
        }
        System.out.println("文字列s5で最初に'Java'が登場する位置は" + s5.indexOf("Java"));
        System.out.println("文字列s5で最後に'Java'が登場する位置は" + s5.lastIndexOf("Java"));

        System.out.println("文字列s6の4文字目以降は" + s6.substring(3));
        System.out.println("文字列s6の4～8文字目は" + s6.substring(3, 8));

        System.out.println("文字列s7を大文字に変換すると " + s7.toUpperCase());
        System.out.println("文字列s7を小文字に変換すると " + s7.toLowerCase());

        // trim => 全角のスペースは除去されない
        System.out.println(
            "文字列s8の前後のスペースを削除すると 『"
            + s8.trim()
            + "』となる。");

        // 存在する文字列は全て置換する
        System.out.println("文字列s9の置換後の文字列は" + s9.replace("1", ""));

        // 存在する文字列は全て置換する(正規表現を使用する場合)
        String w = s10.replaceAll("[beh]", "X");
        System.out.println("文字列s10の置換後の文字列(正規表現)は" + w);

        // 正規表現で , と : を分割した文字列にする [abc->def->ghi->]
        String[] words = s10.split("[,:]");
        for (String w2: words) {
            System.out.println("文字列s10の分割後の文字列(正規表現)は" + w2);
        }

        // 正規表現でnameのバリデーションを行う
        Valid v = new Valid();
        boolean result = v.isValidPlayerName(name);
        System.out.println("バリデーションの結果は" + result + "です");

        // 文字列を1文字ずつfor文でループして判定を行う
        for (int i = 0; i < s11.length()-1; i++) {
            // ループのインデックスで文字列の順で数えてchar変数に代入
            char temp = s11.charAt(i);
            System.out.println("temp:" + temp);

            if (temp == 'M' || temp == 'F') {
                System.out.println("No");
                break;
            }
        }

    }
}
