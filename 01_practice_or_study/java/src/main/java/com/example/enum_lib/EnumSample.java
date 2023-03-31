package com.example.enum_lib;

enum EnumSample {
    /*
     * Orange, Apple, Melonという値のみ返したい場合の定義方法
     */
    Orange,
    Apple,
    Melon
}

enum EnumSample2 {
    /*
     * Orange, Apple, Melonのキーに紐づく数値を返したい場合の定義方法
     * コンストラクタのアクセス修飾子はprivateのみ使用可能。
     * コンストラクタの処理を記述しない場合はエラーが発生する為、注意。
     * コンストラクタの記述は値を保持するために必要。
     */
    Orange(1),
    Apple(2),
    Melon(3);
    
    private final int id;
    
    // コンストラクタの定義
    private EnumSample2(final int id) {
        this.id = id;
    }

    public int getInt() {
        return this.id;
    }
}

enum EnumSample3 {
    /*
     * Orange, Apple, Melonのキーに紐づく文字列を返したい場合の定義方法
     * コンストラクタのアクセス修飾子はprivateのみ使用可能。
     * コンストラクタの処理を記述しない場合はエラーが発生する為、注意。
     * コンストラクタの記述は値を保持するために必要。
     */
    Orange("Ehime"),
    Apple("Aomori"),
    Melon("Ibaraki");
    
    private final String name;

    // コンストラクタの定義
    private EnumSample3(final String name) {
        this.name = name;
    }

    public String getValue() {
        return this.name;
    }
}

enum EnumSample4 {
    /*
     * Orange, Apple, Melonのキーに紐づく文字列を返したい場合の定義方法
     * コンストラクタのアクセス修飾子はprivateのみ使用可能。
     * コンストラクタの処理を記述しない場合はエラーが発生する為、注意。
     * コンストラクタの記述は値を保持するために必要。
     */
    Orange("Ehime", 10),
    Apple("Aomori", 20),
    Melon("Ibaraki", 30);
    
    private final String name;
    private final int id;

    // コンストラクタの定義
    private EnumSample4(final String name, final int id) {
        this.name = name;
        this.id = id;
    }

    public String getValue() {
        return this.name;
    }

    public int getInt() {
        return this.id;
    }
}


