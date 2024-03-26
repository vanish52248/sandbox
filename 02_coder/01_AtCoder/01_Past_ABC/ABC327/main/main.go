package main

import "fmt"

func main() {
	var N int
	var S string

	fmt.Scan(&N, &S)

	current := string(S[0])
	for i := 1; i < N; i++ {
		if (string(S[i]) == "a" && current == "b") || (current == "a" && string(S[i]) == "b") {
			fmt.Println("Yes")
			return
		}
		current = string(S[i])
	}
	fmt.Println("No")
}
