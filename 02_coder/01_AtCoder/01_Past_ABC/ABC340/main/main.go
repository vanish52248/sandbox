package main

import "fmt"

func main() {
	var A, B, D int
	fmt.Scan(&A, &B, &D)

	for i := A; i <= B; i += D {
		fmt.Print(i, " ")
	}
}
