package com.example.generic_lib;

// ①型が<E>のクラスを定義する(後から型を使いまわす場合)
public class GenericSample<E> {
    /*
     * ジェネリクス(総称型)型のクラス定義
     */
    // ②メンバ変数としてクラスで定義した<E>型の変数を定義する
    private E data;

    // ③setterとして<E>型の変数にセットする
    public void setE(E data) {
        this.data = data;
    }

    // ④getterとして<E>型の変数を返す
    public E getE() {
        return this.data;
    }
}
