package main

import (
	"fmt"
	"math"
)

func main() {
	var A, B int
	fmt.Scan(&A, &B)
	fmt.Println(int(math.Pow(float64(A), float64(B)) + math.Pow(float64(B), float64(A))))
}
