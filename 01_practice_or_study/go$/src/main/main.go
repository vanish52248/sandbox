package main

import "fmt"

// 暗黙的な変数定義の場合は関数内で宣言不可(明示的な変数宣言はOK)
// i5 := 500
var i5 int = 500

func outer() {
	var s4 string = "outer"
	fmt.Println(s4)
}

func main() {
	// 明示的な定義
	var i int = 100
	fmt.Println(i)

	var s string = "Hello Go"
	fmt.Println(s)

	var t, f bool = true, false
	fmt.Println(t, f)

	var (
		i2 int    = 200
		s2 string = "Golang"
	)
	fmt.Println(i2, s2)

	var i3 int
	var s3 string
	fmt.Println(i3, s3)

	i3 = 300
	s3 = "Go"
	fmt.Println(i3, s3)

	i = 150
	fmt.Println(i)

	fmt.Println("================================================")

	// 暗黙的な定義
	i4 := 400
	fmt.Println(i4)

	i4 = 450
	fmt.Println(i4)

	// 再定義はエラーになる
	// i4 := 500

	// 型違いでエラーになる
	// i4 = "Hello"

	fmt.Println(i5)

	// 関数外の変数定義の変数を使用しようとするとスコープ外の為エラー
	// fmt.Println(s4)
	outer()

	// GOは変数定義されたものは未使用のままだとエラーになる
	// var s5 string = "Not Use"

}
