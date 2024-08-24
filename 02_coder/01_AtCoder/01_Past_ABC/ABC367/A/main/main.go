package main

import "fmt"

func main() {
	var A, B, C int
	fmt.Scan(&A, &B, &C)

	if B < C {
		if A <= B || C <= A {
			fmt.Println("Yes")
		} else {
			fmt.Println("No")
		}
	} else {
		if C < A && A < B {
			fmt.Println("Yes")
		} else {
			fmt.Println("No")
		}
	}
}
