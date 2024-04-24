package main

import "fmt"

func main() {
	var A, B int

	fmt.Scan(&A, &B)

	calc := A + B

	for i := 0; i <= 9; i++ {
		if i != calc {
			fmt.Println(i)
			break
		}
	}
}
