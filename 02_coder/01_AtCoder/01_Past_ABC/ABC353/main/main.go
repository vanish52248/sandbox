package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)

	list := []int{}
	for i := 0; i < N; i++ {
		var H int
		fmt.Scan(&H)

		list = append(list, H)
	}

	high := list[0]
	for i, v := range list {
		if high < v {
			fmt.Println(i + 1)
			return
		}
	}
	fmt.Println(-1)
}
