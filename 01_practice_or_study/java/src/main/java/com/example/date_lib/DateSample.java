package com.example.date_lib;

import java.time.*;

public class DateSample {
    public static void main(String[] args) {
        // LocalDateTimeの生成方法
        LocalDateTime l1 = LocalDateTime.now(); // 現在日時を取得
        System.out.println("現在の日時は、" + l1);
        LocalDateTime l2 = LocalDateTime.of(2023, 3, 28, 12, 36);
        System.out.println("指定した日時は、" + l2);

        // LocalDateTimeとZonedDateTimeの相互変換
        ZonedDateTime z1 = l2.atZone(ZoneId.of("Europe/London"));
        System.out.println("ZonedDateTime情報への変換後は、" + z1);
        LocalDateTime l3 = z1.toLocalDateTime();
        System.out.println("LocalDateTime情報への変換後は、" + l3);
    }
}
