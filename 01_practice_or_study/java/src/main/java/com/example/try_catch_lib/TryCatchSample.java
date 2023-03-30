package com.example.try_catch_lib;

import java.io.*;

public class TryCatchSample {
    public static void main(String[] args) {
        /*
        * クローズしなければならないリソースを扱う場合は, 下記try-with-resourceを使う
        * 例) ファイル操作やデータベース接続、ネットワーク接続など
        */
        try(FileWriter fw = new FileWriter("data.txt")) {
            fw.write("data.txtファイルへの記載内容");
        } catch (Exception e) {
            System.out.println("何らかの例外が発生しました =>" + e);
        }

        Person p = new Person();
        // 例外を起こす
        try {
            p.setAge(-1);
        } catch (Exception e) {
            System.out.println("年齢は正の整数を指定すべき");
        }
    }
}

class Person {
    int age;
    public void setAge(int age) {
        if (age < 0) {
            throw new IllegalArgumentException();
        }
        this.age = age;
    }
}
