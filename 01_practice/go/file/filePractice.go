package main

import (
	"fmt"
	"os"
)

// ファイルの作成
func createFile(p string) *os.File {
	fmt.Println("creating")

	// ファイルの作成
	// 引数でもらった名前のファイルを実行ディレクトリに作成する
	f, err := os.Create(p)

	if err != nil {
		panic(err)
	}
	return f
}

// ファイルへの書き込み
func writeFile(f *os.File) {
	fmt.Println("writing")

	// ファイルへの書き込み
	// 第一引数=>書き込み先 第二引数=>書き込み内容
	fmt.Fprintln(f, "test")
}

// ファイルを閉じる
func closeFile(f *os.File) {
	fmt.Println("closing")

	// ファイルを閉じる
	err := f.Close()

	if err != nil {
		fmt.Fprintf(os.Stderr, "error: %v\n", err)
		os.Exit(1)
	}
}

func main() {

	// ①ファイルを作成
	f := createFile("temp.txt")

	// 処理後最後に呼ばれる
	// ③ファイルを閉じる
	defer closeFile(f)

	// ②ファイルに書き込む
	writeFile(f)
}
