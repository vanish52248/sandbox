package main

import "fmt"

func main() {
	var N, L int
	fmt.Scan(&N, &L)

	count := 0
	for i := 0; i < N; i++ {
		var A int
		fmt.Scan(&A)
		if L <= A {
			count++
		}
	}
	fmt.Println(count)
}
