package com.example.csv_lib;
import java.util.*;

public class CSVSample {
    public static void main(String[] args) {
        // カンマ区切りで文字列を定義
        String s = "ミナト,アサカ,スガワラ";

        // 第二引数でデリミタとしてカンマを指定
        StringTokenizer st = new StringTokenizer(s, ",");

        // 次のトークンがあるかを判定
        while (st.hasMoreTokens()) {
            String t = st.nextToken();
            System.out.println(t);
        }
    }
}
