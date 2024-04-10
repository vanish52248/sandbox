package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)

	word := "L"
	for i := 0; i < N; i++ {
		word += "o"
	}
	word += "ng"

	fmt.Println(word)
}
