package main

import (
	"fmt"
	"math"
)

func main() {
	var A, B int
	totalA := 0
	totalB := 0
	for i := 0; i < 9; i++ {
		fmt.Scan(&A)
		totalA += int(A)
	}
	for i := 0; i < 8; i++ {
		fmt.Scan(&B)
		totalB += int(B)
	}

	fmt.Println(math.Abs(float64(totalA - totalB + 1)))
}
