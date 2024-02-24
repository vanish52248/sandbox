package main

import "fmt"

func main() {
	var A, B int
	fmt.Scan(&A, &B)

	if 1 <= A && 3 >= B && (B-1) == A || 4 <= A && 6 >= B && (B-1) == A || 7 <= A && 9 >= B && (B-1) == A {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
