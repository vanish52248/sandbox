package main

import "fmt"

func main() {

	// make関数でmapの作成
	fruitsPriceMap := make(map[string]int)

	// mapに値を設定
	fruitsPriceMap["apple"] = 200
	fruitsPriceMap["banana"] = 150
	fruitsPriceMap["orange"] = 100
	fmt.Println("map:", fruitsPriceMap)

	// キー存在確認テスト
	// キーで指定する際には第二引数にステータスが設定される(ok)
	// キーがない場合は ok = false になるのでそこでキー存在有無を判定
	key := "appleeeeee"
	value, ok := fruitsPriceMap[key]

	fmt.Println("value:", value, "exists:", ok)

	// キー存在確認で分岐する場合
	if ok {
		fmt.Println("存在する為valueを表示: ", value)
	} else {
		fmt.Println(key, "というキーは存在しません。")
	}

	// キーバリューセットのforループ
	// key, value については使用しない場合 _ で省略も可能
	for key, value := range fruitsPriceMap {
		fmt.Println("key:", key, "value:", value)
	}
}
