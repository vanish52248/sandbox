package main

import (
	"fmt"
)

func main() {
	var a, b, c, d int
	fmt.Scanf("%d %d %d %d\n", &a, &b, &c, &d)

	fmt.Println(Max(a*b, c*d))
}

func Max(a int, b int) int {
	if a > b {
		return a
	} else if a < b {
		return b
	} else {
		return a
	}
}
