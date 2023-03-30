package com.example.object_lib;

public class ObjectSample {
    public static void main(String[] args) {
        Person p = new Person();
        // 初期化された値を出力
        // 暗黙的にSystem.out.println(p.toString())になる
        System.out.println("① " + p);
        p.setAge(20);
        p.setName("hirano");
        // 設定後の値を出力
        // 暗黙的にSystem.out.println(p.toString())になる
        System.out.println("② " + p);

        // "clone()でインスタンスを複製
        Person p2 = p.clone();
        p.setAge(30);
        p.setName("mikado");
        // シャローコピー(参照のコピー)ではなくディープコピー(値のみのコピー)になっていることを確認
        System.out.println("④ 変更した方 " + p);
        System.out.println("④ 変更してない方 " + p2);
    }
}
