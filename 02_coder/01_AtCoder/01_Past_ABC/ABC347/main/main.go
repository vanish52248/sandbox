package main

import "fmt"

func main() {
	var N, K int
	fmt.Scan(&N, &K)

	for i := 0; i < N; i++ {
		var A int
		fmt.Scan(&A)

		if A%K == 0 {
			fmt.Print(A/K, " ")
		} else {
			continue
		}
	}
}
