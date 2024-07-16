package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)

	count := 0
	for i := 0; i < N; i++ {
		var S string
		fmt.Scan(&S)
		if S == "Takahashi" {
			count++
		}
	}
	fmt.Println(count)
}
