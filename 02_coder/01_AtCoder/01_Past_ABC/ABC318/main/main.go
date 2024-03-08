package main

import (
	"fmt"
)

func main() {
	var N, M, P int
	fmt.Scan(&N, &M, &P)

	count := 0
	for i := M; i <= N; i += P {
		count++
	}
	fmt.Println(count)
}
