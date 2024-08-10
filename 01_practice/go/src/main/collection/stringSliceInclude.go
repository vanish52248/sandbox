package main

import "fmt"

// Index は文字列 t を始めに見つけたインデックスを返す。
// もし見つからなければ -1 を返す。
func Index(vs []string, t string) int {
	for i, v := range vs {
		if v == t {
			return i
		}
	}
	return -1
}

// Include はスライスの中に文字列 t が含まれるなら true を返す。
func Include(vs []string, t string) bool {
	return Index(vs, t) >= 0
}

func main() {
	// 検索対象のスライス
	sampleList := []string{"ABC", "DEF", "XYZ"}

	// 第一引数のリストの中から第二引数の単語を検索する
	// 存在する=>true 存在しない=>false
	IsWord := Include(sampleList, "AB")

	fmt.Println(IsWord)
}
