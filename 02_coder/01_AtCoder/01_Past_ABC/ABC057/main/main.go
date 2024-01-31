package main

import (
	"fmt"
	"math"
)

func main() {
	var A, B int
	fmt.Scanf("%d %d\n", &A, &B)

	if A+B >= 24 {
		fmt.Println(math.Abs(24 - float64((A + B))))
	} else {
		fmt.Println(math.Abs(float64((A + B))))
	}
}
