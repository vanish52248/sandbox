package main

import (
	"fmt"
	"math"
)

func main() {
	var N, T, A float64

	fmt.Scan(&N, &T, &A)

	remaining := (N - (T + A))
	if math.Max(T, A) > math.Min(T, A)+float64(remaining) {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
