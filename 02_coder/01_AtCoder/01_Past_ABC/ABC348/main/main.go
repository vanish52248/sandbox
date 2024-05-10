package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)

	for i := 1; i <= N; i++ {
		if i%3 == 0 {
			fmt.Print("x")
		} else {
			fmt.Print("o")
		}
	}
}
