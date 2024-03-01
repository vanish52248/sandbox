package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)

	list := []int{}
	for i := 0; i < N; i++ {
		var P int
		fmt.Scan(&P)
		list = append(list, P)
	}
	maxIdx, maxNum := maxNumber(list)

	if maxIdx == 0 {
		fmt.Println(0)
	} else {
		fmt.Println(maxNum - list[0] + 1)
	}
}

func maxNumber(list []int) (int, int) {
	result := 0
	index := 0
	for i, v := range list {
		if result <= v {
			result = v
			index = i
		}
	}
	return index, result
}
