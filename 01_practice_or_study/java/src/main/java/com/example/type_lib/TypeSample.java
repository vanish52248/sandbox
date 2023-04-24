package com.example.type_lib;

public class TypeSample {
    public static void main(String[] args) {
        String s = "abc";
        double d = 3.14;
        int n = 5;
        boolean t = true;

        // String以外のプリミティブ型はオブジェクト型へのキャストが必要
        String type_s = s.getClass().getSimpleName();
        String type_d = ((Object)d).getClass().getSimpleName();
        String type_n = ((Object)n).getClass().getSimpleName();
        String type_t = ((Object)t).getClass().getSimpleName();

        System.out.println(type_s);
        System.out.println(type_d);
        System.out.println(type_n);
        System.out.println(type_t);
    }
}
