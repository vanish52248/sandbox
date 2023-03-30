package com.example;

public class Score {

    public String judgeGrade(int score) {
        if (score < 0) {
            throw new IllegalArgumentException("score は 0点以上にするべきです。:" + score);
        } else if (score > 100) {
            throw new IllegalArgumentException("score は 100点以下にするべきです。:" + score);
        }
        if (score < 70) {
            return "C";
        } else if (score < 80) {
            return "B";
        } else if (score < 90) {
            return "A";
        } else {
            return null;
        }
    }
}
