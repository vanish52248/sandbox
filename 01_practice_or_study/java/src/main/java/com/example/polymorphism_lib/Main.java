package com.example.polymorphism_lib;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        // ①Flower型の可変配列を作り、子要素インスタンスを格納
        List<Flower> flowers = new ArrayList<>();
        flowers.add(new SunFlower());
        flowers.add(new NightFlower());

        // ②Flower型の可変配列をループで回し、それぞれメソッドを呼び出す
        for (Flower flower: flowers) {
            flower.bloom();
        }
    }
}
