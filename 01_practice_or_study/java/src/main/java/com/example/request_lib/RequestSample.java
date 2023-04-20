package com.example.request_lib;

import java.io.*;
import java.net.*;

public class RequestSample {
    public static void main(String[] args) {
        try {
            // 通信するURL
            URL url = new URL("http://google.com");
            InputStream is = url.openStream();
            InputStreamReader isr = new InputStreamReader(is);
            int i = isr.read();
            while (i != -1) {
                System.out.print((char)i);
                i = isr.read();
            }
            isr.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
