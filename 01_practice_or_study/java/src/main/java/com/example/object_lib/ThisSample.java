package com.example.object_lib;

public class ThisSample {
    /*
     * thisを使えるのはインスタンスのコンテキスト内のみ。
     * staticメソッド・staticイニシャライザなどではthisを使うとコンパイルエラーになる。
     * staticなコンテキスト内では、紐付いているインスタンスがない為。
     */
    public static void main(String[] args) {
        // 変数代入しない場合はnew クラス名だけでもインスタンス化出来る
        new ThisSample2();
    }
}

class ThisSample2 {
    ThisSample2() {
        System.out.println("ThisSample2を呼び出しました。");
        // 自インスタンスのメソッドを呼ぶ
        this.actionSample("fuga");
        // this. を省略しても呼び出し可能
        actionSample();
    }

    private void actionSample() {
        System.out.println("① hogeを表示します。");
    }

    private void actionSample(String word) {
        System.out.println("② " + word + "を表示します。");
    }
}
