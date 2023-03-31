package com.example.enum_lib;

public class Main {
    public static void main(String[] args) {
        /*
         * EnumSample1(キーのみの定義)
         */
        // enumのキー取得(Melon)
        System.out.println("EnumSample1: " + EnumSample.Melon);
        System.out.println();


        /*
         * EnumSample2(キーと数値の値の定義)
         */
        // enumのキー取得(Orange)
        EnumSample2 enumSample2 = EnumSample2.Orange;
        System.out.println("EnumSample2: " + enumSample2);

        // enumの数値の値取得(2)
        System.out.println("EnumSample2: " + EnumSample2.Apple.getInt());
        System.out.println();


        /*
         * EnumSample3(キーと文字列の値の定義)
         */
        // enumのキー取得(Orange)
        EnumSample3 enumSample3 = EnumSample3.Orange;
        System.out.println("EnumSample3: " + enumSample3);
        
        // enumの文字列の値取得(Aomori)
        System.out.println("EnumSample3: " + EnumSample3.Apple.getValue());
        System.out.println();


        /*
         * EnumSample4(キーと複数の値の定義)
         */
        // enumのキー取得(Melon)
        EnumSample4 enumSample4 = EnumSample4.Melon;
        System.out.println("EnumSample4: " + enumSample4);
        
        // enumの文字列の値取得(Ibaraki)
        System.out.println("EnumSample4: " + EnumSample4.Melon.getValue());
        // enumの数値の値取得(20)
        System.out.println("EnumSample4: " + EnumSample4.Apple.getInt());
    }
}
