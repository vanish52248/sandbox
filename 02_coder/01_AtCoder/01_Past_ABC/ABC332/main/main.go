package main

import "fmt"

func main() {
	var N, S, K int
	fmt.Scan(&N, &S, &K)

	price := 0
	for i := 0; i < N; i++ {
		var P, Q int
		fmt.Scan(&P, &Q)

		price += P * Q
	}
	if price >= S {
		fmt.Println(price)
	} else {
		fmt.Println(price + K)
	}
}
