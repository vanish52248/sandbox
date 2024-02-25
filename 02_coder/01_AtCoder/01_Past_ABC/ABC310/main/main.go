package main

import "fmt"

func main() {
	var N, P, Q int
	fmt.Scan(&N, &P, &Q)

	var NList []int

	for i := 0; i < N; i++ {
		var D int
		fmt.Scan(&D)
		NList = append(NList, D)
	}

	minPrice := calcMinNumber(NList)

	if P >= Q+minPrice {
		fmt.Println(Q + minPrice)
	} else {
		fmt.Println(P)
	}
}

func calcMinNumber(N []int) int {
	minNumber := N[0]
	for _, v := range N {
		if minNumber > v {
			minNumber = v
		}
	}
	return minNumber
}
