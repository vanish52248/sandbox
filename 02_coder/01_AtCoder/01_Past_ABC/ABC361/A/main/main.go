package main

import "fmt"

func main() {
	var N, K, X int
	fmt.Scan(&N, &K, &X)

	list := make([]int, 0, N+1)
	for i := 0; i < N; i++ {
		var A int
		fmt.Scan(&A)

		list = append(list, A)
	}

	list = append(list[:K+1], list[K:]...)
	list[K] = X

	for _, v := range list {
		fmt.Print(v, " ")
	}
}
