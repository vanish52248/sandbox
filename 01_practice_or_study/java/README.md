# 前提
* ビルドツール: mavenプロジェクト

# javaファイルコンパイルと実行方法

## ①パッケージの宣言を以下2種類で行っている
```
com.example;
com.example.hogehoge;
```

## ②コンパイルと実行する際は、パッケージが格納されているディレクトリで移動
```
cd sandbox/01_practice_or_study/java/src/main/java
```

## ③コンパイルと実行
```
# 1.Mainを実行するケース
javac com/example/Main.java && java com/example/Main

# 2.lib配下のクラスを実行するケース
javac com/example/str_lib/StrSample.java && com/example/str_lib/StrSample
```



# javaファイルのJunit(UT)実行方法とJacoco(カバレッジ)取得方法

## ①UT実行する際はpom.xmlがある階層に移動
```
cd sandbox/01_practice_or_study/java
```

## ②それぞれのパターンでUT実行
```
# test配下全てのクラスのテスト実行
mvn test

# test配下の指定したクラスのみテスト実行
mvn test -Dtest=ScoreTest.java

# test配下の指定したクラスの指定したメソッドのみ実行
mvn test -Dtest=ScoreTest#raiseScore1
```
※ VSCodeの機能でTestingペインからテスト実行も可能

## ③カバレッジ取得する際はpom.xmlがある階層に移動
```
cd sandbox/01_practice_or_study/java
```

## ④カバレッジレポートの取得
```
# test配下全てのクラスのカバレッジ取得
mvn test jacoco:report

# test配下の指定したクラスのみカバレッジ取得
mvn test -Dtest=ScoreTest.java jacoco:report
```
