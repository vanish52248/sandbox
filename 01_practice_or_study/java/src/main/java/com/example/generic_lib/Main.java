package com.example.generic_lib;

public class Main {
    public static void main(String[] args) {
        // ①インスタンス化する際に<E>型を任意の型に変更してインスタンス化を行う
        GenericSample<String> g = new GenericSample<>();

        // ②インスタンス化したオブジェクトに対して値をセットする(文字列定義なら文字列)
        g.setE("ジェネリクス型のサンプル");
        System.out.println("<E>が<String>の場合:" + g.getE());

        // ③インスタンス化する際に<E>型を任意の型に変更してインスタンス化を行う
        GenericSample<Integer> g2 = new GenericSample<>();

        // ④インスタンス化したオブジェクトに対して値をセットする(数値定義なら数値)
        g2.setE(1000);
        System.out.println("<E>が<Integer>の場合:" + g2.getE());
    }
}
