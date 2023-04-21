package com.example.thread_lib;

import java.util.*;

class PrintingThread extends Thread {
    public void run() {
        /*
         * run()を実行し終えるとスレッドは自動的に消滅するのでPGが停止や消滅を指示する必要なし
         */
        for (int i = 0; i <= 100; i++) {
            System.out.println(i);
        }
    }
}


public class ThreadSample {
    public static void main(String[] args) {
        /*
         * スレッドの使い方（並列処理のためのJVMを増やす方法）
         * ①Threadクラスを継承しrunメソッドをオーバーライドする。
         *  →このとき run()にはスレッドで処理したい内容を書き込む。
         * ②別スレッドの実行を開始したい場所で①のクラスをインスタンス化し、 start() メソッドを呼び出す。
         * 
         */
        System.out.println("何か入力してください。");
        Thread t = new PrintingThread();
        // 別スレッドを開始
        t.start();
        new Scanner(System.in).nextLine();
    }
}
