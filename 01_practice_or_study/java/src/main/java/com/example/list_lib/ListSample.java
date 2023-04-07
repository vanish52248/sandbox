package com.example.list_lib;

import java.util.*;

public class ListSample {
    public static void main(String[] args) {
        // 標準入力
        Scanner sc = new Scanner(System.in);
        final String N = sc.next();

        String[] numArray = new String[Integer.parseInt(N)];
    	for(int i = 0; i < numArray.length; i++) {
    		numArray[i] = sc.next();
    	}

        List<String> sl = new ArrayList<>();
        for (int i = 0; i < numArray.length; i++) {
            if (Integer.parseInt(numArray[i]) %2 == 0) {
                sl.add(numArray[i]);
            }
        }

        // ★配列をスペース区切りで[]なしで文字列に設定する記述
        String res = String.join(" ",  sl);
        System.out.println(res);


        sc.close();
    }
}
