package com.example.file_lib;

import java.io.*;

public class FileSample {
    public static void main(String[] args) throws IOException{
        // 第二引数のtrue が追記 falseが上書き
        FileWriter fw = new FileWriter("./com/example/file_lib/file.dat", true);
        fw.write("ABCDEFG");
        fw.flush();
        fw.close();


        FileReader fw2 = new FileReader("./com/example/file_lib/file.dat");
        System.out.println("全てのデータを読み込んで表示します。");
        int i = fw2.read();
        while(i != -1) {
            char c = (char)i;
            System.out.println(c);
            i = fw2.read();
        }
        System.out.println("ファイルの末尾に到達");
        fw2.close();
    }
}
