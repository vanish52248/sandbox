package com.example.try_catch_lib;

class OriginalExceptionSample extends Exception{
    // 自作のエラークラス
    // エラーメッセージを受け取るコンストラクタ
    public OriginalExceptionSample(String msg) {
        super(msg);
    }
}


