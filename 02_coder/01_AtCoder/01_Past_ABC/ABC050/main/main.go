package main

import (
	"fmt"
)

func calculate(A, B int, op string) int {
	// 演算子に応じて計算を行う
	if op == "+" {
		return A + B
	} else if op == "-" {
		return A - B
	} else {
		// 予期しない演算子が与えられた場合はエラー値として -1 を返す
		return -1
	}
}

func main() {
	// 入力の変数を定義
	var A, B int
	var op string

	// 整数 A を入力
	fmt.Scan(&A)

	// 演算子 op を入力
	fmt.Scan(&op)

	// 整数 B を入力
	fmt.Scan(&B)

	// 計算結果を求める
	result := calculate(A, B, op)

	// 結果を出力
	fmt.Println(result)
}
