package main

import "fmt"

func main() {
	var N int
	var S string
	fmt.Scan(&N, &S)

	for i := 0; i < N; i++ {
		fmt.Print(string(S[i]) + string(S[i]))
	}
}
