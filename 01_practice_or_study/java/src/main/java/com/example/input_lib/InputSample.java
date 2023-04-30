package com.example.input_lib;

import java.util.*;

public class InputSample {
    /*
     * キーボードからの入力のサンプルクラス
     * 試したい時、必要に応じてコメントアウト(解除)する。
     */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 1 2 3
        // ->  1 2 3
        // 数値一行スペース区切りのインプット
        // int N1 = sc.nextInt();
        // int N2 = sc.nextInt();
        // int N3 = sc.nextInt();
        // System.out.println("N1:" + N1 + "  N2:" + N2 + "  N3:" + N3);


        // N
        // 1 2 3...N
        // -> [1, 2, 3...N] 
        // N個の数値一行スペース区切りのインプットをリスト格納
        // int N4 = sc.nextInt();
        // List<Integer> C = new ArrayList<>();
        // for (int i = 0; i < N4; i++) {
        //     C.add(sc.nextInt());
        // }
        // System.out.println("C:" + C);

        // abc
        // -> [a, b, c]
        // 文字列インプットを位置文字ずつリスト格納([a, b, c] ->join-> abc)
        String[] S = sc.nextLine().split("");
        System.out.println(Arrays.toString(S));
        System.out.println(String.join("", S));

        sc.close();
    }
}
