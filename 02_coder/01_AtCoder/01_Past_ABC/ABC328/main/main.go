package main

import (
	"fmt"
)

func main() {
	var N, X int
	fmt.Scan(&N, &X)

	point := 0
	for i := 0; i < N; i++ {
		var S int
		fmt.Scan(&S)
		if S <= X {
			point += S
		}
	}
	fmt.Println(point)
}
