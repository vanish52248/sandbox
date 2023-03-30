package com.example.try_catch_lib;

public class Main {
    public static void main(String[] args) {
        try {
            // 試験的に例外を発生させる
            throw new OriginalExceptionSample("自作例外クラスです。");
        } catch (OriginalExceptionSample e) {
            e.printStackTrace();
        }
    }
}

