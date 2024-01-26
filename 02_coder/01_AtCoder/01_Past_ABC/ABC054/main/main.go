package main

import "fmt"

func main() {
	var A, B int
	fmt.Scanf("%d %d\n", &A, &B)

	if A == 1 {
		A = 14
	}

	if B == 1 {
		B = 14
	}

	if A == B {
		fmt.Println("Draw")
	} else if A > B {
		fmt.Println("Alice")
	} else if A < B {
		fmt.Println("Bob")
	}
}
