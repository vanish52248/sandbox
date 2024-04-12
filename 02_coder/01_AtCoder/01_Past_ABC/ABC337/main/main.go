package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)

	totalX := 0
	totalY := 0
	for i := 0; i < N; i++ {
		var X, Y int
		fmt.Scan(&X, &Y)

		totalX += X
		totalY += Y
	}

	if totalX > totalY {
		fmt.Println("Takahashi")
	} else if totalX < totalY {
		fmt.Println("Aoki")
	} else {
		fmt.Println("Draw")
	}
}
