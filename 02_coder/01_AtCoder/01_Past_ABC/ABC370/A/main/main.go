package main

import "fmt"

func main() {
	var L, R int
	fmt.Scan(&L, &R)

	if (L == 1 && R == 1) || (L == 0 && R == 0) {
		fmt.Println("Invalid ")
	} else if L == 1 {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
