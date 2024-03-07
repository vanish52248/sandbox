package main

import "fmt"

func main() {
	var N, H, X int
	fmt.Scan(&N, &H, &X)

	var list = []int{}
	for i := 0; i < N; i++ {
		var P int
		fmt.Scan(&P)
		list = append(list, P)
	}

	currentMin := 1000
	idx := 0
	for i, v := range list {
		if H+v < X {
			continue
		}
		if currentMin >= v {
			idx = i + 1
			currentMin = v
		}
	}
	fmt.Println(idx)
}
